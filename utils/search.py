import email
import logging

import httpx
from lxml import objectify, etree

from utils.envelops import SEARCH_ENVELOPE, LOGIN_ENVELOPE
from errors import REGONAPIError
from utils.parsing import xml_to_json

from config import CONFIG

SERVICE_URL = CONFIG["accessing"]["service_url"]
USER_KEY = CONFIG["accessing"]["user_key"]
namespaces = CONFIG["namespaces"]

log = logging.getLogger(__name__)


def get_message_element(message, payload_num, path):
    resp = message.get_payload(payload_num).get_payload()
    return etree.fromstring(resp).xpath(path, namespaces=namespaces)


class RegonAPI:
    def __init__(self, service_url):
        self.service_url = service_url
        self.sid = None

    async def call(self, envelope, **kwargs):
        data = envelope.format(api=self, **kwargs)
        log.debug("Data to be posted: %s", data)

        headers = {
            "Content-Type": "application/soap+xml; charset=utf-8",
        }
        if self.sid:
            headers["sid"] = self.sid
        async with httpx.AsyncClient() as client:
            res = await client.post(SERVICE_URL, data=data, headers=headers)

            mimemsg = "\r\n".join(
                "{0}: {1}".format(key, val) for key, val in res.headers.items()
            )
            mimemsg += "\r\n" + res.text
            msg = email.message_from_string(mimemsg)
            assert msg.is_multipart(), "Response is not multipart."

            return msg

    async def search(
        self,
        nip=None,
        regon=None,
        krs=None,
        nips=None,
        regons=None,
        krss=None,
    ):
        if not (regon or nip or krs or regons or nips or krss):
            raise REGONAPIError(
                "You have to pass at least one of: "
                "nip(s), regon(s) or krs(s) parameters.",
                400,
            )

        param = ""
        if nip:
            param += "<dat:Nip>{0}</dat:Nip>".format(nip)

        if regon:
            param += "<dat:Regon>{0}</dat:Regon>".format(regon)

        if krs:
            param += "<dat:Krs>{0}</dat:Krs>".format(krs)

        if nips:
            nip_str = "".join(nips)
            assert len(nip_str) % 10 == 0, "All NIPs should be 10 character strings."

            param += "<dat:Nipy>{0}</dat:Nipy>".format(nip_str)

        if krss:
            krs_str = "".join(krss)
            assert len(krs_str) % 10 == 0, "All KRSs should be 10 character strings."
            param += "<dat:Krsy>{0}</dat:Krsy>".format(krs_str)

        if regons:
            regons_str = "".join(regons)
            rl = len(regons_str)

            if rl % 9 == 0:
                param += "<dat:Regony9zn>{0}</dat:Regony9zn>".format(regons_str)
            elif rl % 14 == 0:
                param += "<dat:Regony14zn>{0}</dat:Regony14zn>".format(regons_str)
            else:
                raise AssertionError(
                    "All REGONs should be either 9 or 14 character strings.", 400
                )

        msg = await self.call(SEARCH_ENVELOPE, param=param)
        result = get_message_element(msg, 0, "//bir:DaneSzukajPodmiotyResult/text()")

        if not result:
            raise REGONAPIError("No response received. Are you logged in?", 401)
        dane_obj = objectify.fromstring(result[0]).dane

        try:
            sr = dane_obj
            code = sr.ErrorCode[0]
            message = sr.ErrorMessageEn[0]
            raise REGONAPIError(message, code, sr)
        except AttributeError:
            pass

        return xml_to_json(dane_obj)

    async def login(self, user_key):
        msg = await self.call(LOGIN_ENVELOPE, user_key=user_key)
        result = get_message_element(msg, 0, "//bir:ZalogujResult/text()")
        if not result:
            self.sid = None
            raise REGONAPIError("Login failed.", 401)
        self.sid = str(result[0])
        return self.sid

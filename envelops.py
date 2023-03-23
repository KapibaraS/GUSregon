SEARCH_ENVELOPE = """
<soap:Envelope xmlns:soap="http://www.w3.org/2003/05/soap-envelope" xmlns:ns="http://CIS/BIR/PUBL/2014/07" xmlns:dat="http://CIS/BIR/PUBL/2014/07/DataContract">
<soap:Header xmlns:wsa="http://www.w3.org/2005/08/addressing">
<wsa:To>{api.service_url}</wsa:To>
<wsa:Action>http://CIS/BIR/PUBL/2014/07/IUslugaBIRzewnPubl/DaneSzukajPodmioty</wsa:Action>
</soap:Header>
   <soap:Body>
      <ns:DaneSzukajPodmioty>
         <ns:pParametryWyszukiwania>
            {param}
         </ns:pParametryWyszukiwania>
      </ns:DaneSzukajPodmioty>
   </soap:Body>
</soap:Envelope>
"""

FULL_REPORT_ENVELOPE = """
<soap:Envelope xmlns:soap="http://www.w3.org/2003/05/soap-envelope" xmlns:ns="http://CIS/BIR/PUBL/2014/07">
<soap:Header xmlns:wsa="http://www.w3.org/2005/08/addressing">
<wsa:To>{api.service_url}</wsa:To>
<wsa:Action>http://CIS/BIR/PUBL/2014/07/IUslugaBIRzewnPubl/DanePobierzPelnyRaport</wsa:Action>
</soap:Header>
  <soap:Body>
      <ns:DanePobierzPelnyRaport>
         <ns:pRegon>{regon}</ns:pRegon>
         <ns:pNazwaRaportu>{report_name}</ns:pNazwaRaportu>
      </ns:DanePobierzPelnyRaport>
   </soap:Body>
</soap:Envelope>
"""

LOGIN_ENVELOPE = """
<soap:Envelope xmlns:soap="http://www.w3.org/2003/05/soap-envelope" xmlns:ns="http://CIS/BIR/PUBL/2014/07">
<soap:Header xmlns:wsa="http://www.w3.org/2005/08/addressing">
<wsa:To>{api.service_url}</wsa:To>
<wsa:Action>http://CIS/BIR/PUBL/2014/07/IUslugaBIRzewnPubl/Zaloguj</wsa:Action>
</soap:Header>
   <soap:Body>
      <ns:Zaloguj>
         <ns:pKluczUzytkownika>{user_key}</ns:pKluczUzytkownika>
      </ns:Zaloguj>
   </soap:Body>
</soap:Envelope>
"""

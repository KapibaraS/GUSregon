from typing import Optional

from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from fastapi.responses import JSONResponse

from errors import REGONAPIError
from utils.search import RegonAPI, SERVICE_URL, USER_KEY

app = FastAPI()


class RegonData(BaseModel):
    Regon: Optional[int]
    Nip: Optional[int]
    StatusNip: Optional[str]
    Nazwa: Optional[str]
    Wojewodztwo: Optional[str]
    Powiat: Optional[str]
    Gmina: Optional[str]
    Miejscowosc: Optional[str]
    KodPocztowy: Optional[str]
    Ulica: Optional[str]
    NrNieruchomosci: Optional[int]
    NrLokalu: Optional[str]
    Typ: Optional[str]
    SilosID: Optional[int]
    DataZakonczeniaDzialalnosci: Optional[str]
    MiejscowoscPoczty: Optional[str]


@app.get("/regon/{nip}", response_model=RegonData)
async def regon(nip: int):
    api = RegonAPI(SERVICE_URL)
    try:
        await api.login(USER_KEY)
        regon = await api.search(nip=nip)
    except REGONAPIError as e:
        return JSONResponse(
            content=jsonable_encoder(
                {"error": e.message},
            ),
            status_code=e.code,
        )

    return regon


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port="8000")

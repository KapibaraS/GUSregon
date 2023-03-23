### [Create python venv](https://www.freecodecamp.org/news/how-to-setup-virtual-environments-in-python/)  
    
### install requirements
    pip install -r requirements.txt
### entrypoint
    python api.py

#### example request local: 
    http://127.0.0.1:8000/regon/5261040828


### or use docker
    make run

#### example response:
    {
	"Regon": 331501,
	"Nip": 5261040828,
	"StatusNip": "",
	"Nazwa": "GŁÓWNY URZĄD STATYSTYCZNY",
	"Wojewodztwo": "MAZOWIECKIE",
	"Powiat": "m. st. Warszawa",
	"Gmina": "Śródmieście",
	"Miejscowosc": "Warszawa",
	"KodPocztowy": "00-925",
	"Ulica": "ul. Test-Krucza",
	"NrNieruchomosci": 208,
	"NrLokalu": "",
	"Typ": "P",
	"SilosID": 6,
	"DataZakonczeniaDzialalnosci": "",
	"MiejscowoscPoczty": "Warszawa"
    }

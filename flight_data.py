import requests
import datetime as dt

from decouple import config

class FlightData:

    def __init__(self, api_key: str = config("METASEARCH_API_KEY")):
        self.flight_url = "https://api.tequila.kiwi.com"
        self.__api_key = api_key 
        self.today = dt.datetime.now()
        
        
    def get_location_data(self, location: str = "montreal"):
        self.search_location_url = f"{self.flight_url}/locations/query"
        self.location = location
        self.__headers = {
            "apikey": self.__api_key,
            "accept": "application/json"
        }
        self.parameters = {
            "term": self.location,
            "location_types": "airport",
            "active_only": True
        }
        
        self.response = requests.get(
            url = self.search_location_url,
            params= self.parameters,
            headers = self.__headers
        )
        self.response.raise_for_status()
        
        return self.response.json()
        
    
    def flight_search(self, **kwargs: str):
        
        self.search_url = self.flight_url + "/v2/search"

        self.fly_to = kwargs["fly_to"]
        self.date_from = kwargs.get(
            "date_from", 
            self.today.strftime("%d/%m/%Y")
            )
        self.date_to = kwargs["date_to"]
        self.return_from = kwargs["return_from"]
        self.return_to = kwargs["return_to"]
        self.fly_from = kwargs.get("fly_from", "YYZ")
        self.currency = kwargs.get("currency", "CAD")
        
        self.__headers = {
            "apikey": self.__api_key,
            "accept": "application/json"
        }
        
        self.parameters = {
            "fly_from": self.fly_from,
            "fly_to": self.fly_to,
            "date_from": self.date_from,
            "date_to": self.date_to,
            "return_from": self.return_from,
            "return_to": self.return_to,
            "curr": self.currency
        }
        
        response = requests.get(
            url = self.search_url,
            params = self.parameters,
            headers = self.__headers
        )
        
        response.raise_for_status()
        
        return response.json()
        
import requests

from decouple import config

class DataManager:
    
    def __init__(self, api_key = config("SHEET_TOKEN"), spreadsheet = config("SPREADSHEET")):
        self.__spreadsheet = spreadsheet
        self.__api_key = api_key
        self.__headers = {
            "Authorization" : self.__api_key
        }
        
    def get_destination_data(self):
        
        self.response = requests.get(
            url = self.__spreadsheet, 
            headers = self.__headers
            )
        
        self.response.raise_for_status()
        
        return self.response.json()
        
    def update_destination_data(self, data, row_number: int):
        self.data = data
        self.row_number = row_number
        self.response = requests.put(
            url = self.__spreadsheet +f"/{self.row_number}",
            headers = self.__headers,
            json = data
        )
        
        self.response.raise_for_status()
        
        print(self.response)
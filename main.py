from datamanager import DataManager
from flight_data import FlightData

data = DataManager()
flight_search = FlightData()

sheet_data = data.get_destination_data()

destinations = sheet_data["deals"]

def input_airport_data(iata_code: str, index_number: int):
    sheet_row = index_number + 2
    
    iata_code_data = {
        "deal": {
            "iataCode": iata_code
        }
    }

    data.update_destination_data(
        data = iata_code_data, 
        row_number = sheet_row
        )

def get_airport_data(spreadsheet = destinations):
    
    for index, flight in enumerate(destinations):

        city = flight["city"]
        flight_search_data = flight_search.get_location_data(city)
        location_data = flight_search_data["locations"]
        
        try: 
            iata_code = location_data[0]["code"]
            
        except IndexError as error:
            print(f"The {error}.\nThe destination IATA code could not be found.")
            airport_code = input(f"Please enter the airport code for {city}: \n")
            input_airport_data(iata_code = airport_code, index_number = index)
        
        else:
            input_airport_data(iata_code = iata_code, index_number = index)

get_airport_data()



    
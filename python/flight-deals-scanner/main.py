from flight_search import FlightSearch
import urllib3
from dotenv import load_dotenv
from flight_data import FlightData

load_dotenv()

urllib3.disable_warnings()

from data_manager import DataManager
data_manager = DataManager()
sheet_data = data_manager.get_destination_data()

flight_search = FlightSearch()
flight_dataset = FlightData()

for row in sheet_data:
    if row["iataCode"] == "":
        row["iataCode"] = flight_search.get_city_code(row["city"])
data_manager.destination_data = sheet_data
data_manager.update_destination_codes()

flights_data = {}
for row in sheet_data:
    flights_to_city = flight_search.collect_flight_info(row["iataCode"])
    cheapest_flight,cheapest_dates = flight_dataset.find_cheapest_flight(flights_to_city)
    if float(row["lowestPrice"]) > cheapest_flight:
        row["lowestPrice"] = cheapest_flight
        row["dates"] = cheapest_dates

data_manager.destination_data = sheet_data
data_manager.update_price()

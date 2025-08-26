from flight_search import FlightSearch
import urllib3
from dotenv import load_dotenv
from flight_data import FlightData
from notification_manager import NotificationManager

load_dotenv()

urllib3.disable_warnings()

from data_manager import DataManager
data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
users_emails = data_manager.get_customer_emails()

flight_search = FlightSearch()
flight_dataset = FlightData()
email_sender = NotificationManager()

for row in sheet_data:
    if row["iataCode"] == "":
        row["iataCode"] = flight_search.get_city_code(row["city"])
data_manager.destination_data = sheet_data
data_manager.update_destination_codes()

flights_data = {}
for row in sheet_data:
    city_name = row["city"]
    city_iata = row["iataCode"]
    flights_to_city = flight_search.collect_flight_info(city_iata)
    flight_dataset.format_data(city_name,flights_to_city)
    min_price, min_iter = flight_dataset.find_cheapest_flight(city_name)
    if min_price == 0 or flight_dataset.destination_data[city_name] == []:
        break
    startDate = flight_dataset.destination_data[city_name][min_iter]["departureDate"]
    finishDate = flight_dataset.destination_data[city_name][min_iter]["returnDate"]
    message = f"There is a cheap flight from London to {city_name} for {min_price}. Dates: {startDate} - {finishDate}"
    for email in users_emails:
        email_sender.send_message(email,message)


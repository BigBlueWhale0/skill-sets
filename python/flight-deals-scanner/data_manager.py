import os
import requests
from dotenv import load_dotenv

load_dotenv()

SHEETY_ENDPOINT = os.environ.get("ENV_SHEETY_ENDPOINT")
SHEETY_TOKEN = os.environ.get("ENV_SHEETY_TOKEN")

class DataManager:

    def __init__(self):
        self.headers = {
            "Authorization": f"Basic {SHEETY_TOKEN}",
            "Content-Type": "application/json",
        }
        self.destination_data = {}

    def get_destination_data(self):
        sheety_response = requests.get(SHEETY_ENDPOINT, verify=False, headers=self.headers)
        sheety_data = sheety_response.json()
        self.sheety_prices = sheety_data["prices"]
        return self.sheety_prices

    def update_destination_codes(self):
        for city in self.destination_data:
            iata_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(f"{SHEETY_ENDPOINT}/{city['id']}",json=iata_data,verify=False, headers=self.headers)

    def update_price(self):
        for city in self.destination_data:
            price_data = {
                "price": {
                    "lowestPrice": city["lowestPrice"],
                    "dates": city["dates"]
                }
            }
            response = requests.put(f"{SHEETY_ENDPOINT}/{city['id']}",json=price_data,verify=False, headers=self.headers)


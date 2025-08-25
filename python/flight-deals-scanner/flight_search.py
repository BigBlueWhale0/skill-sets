import os
import requests
from dotenv import load_dotenv
from datetime import datetime,timedelta

load_dotenv()

AMADEUS_API_KEY = os.environ.get("ENV_AMADEUS_API_KEY")
AMADEUS_API_SECRET = os.environ.get("ENV_AMADEUS_API_SECRET")
AMADEUS_API_URL_V2 = os.environ.get("ENV_AMADEUS_API_URL","test.api.amadeus.com/v2")
AMADEUS_API_URL_V1 = os.environ.get("ENV_AMADEUS_API_URL","test.api.amadeus.com/v1")

ORIGIN_LOCATION = "LON"

class FlightSearch:

    def __init__(self):
        amadeus_token = self._auth()
        self.headers = {
            "Authorization": f"Bearer {amadeus_token}",
        }

    def _auth(self):
        security_token = f"https://{AMADEUS_API_URL_V1}/security/oauth2/token"
        auth_header = {
            "Content-Type": "application/x-www-form-urlencoded",
        }
        auth_data = {
            "grant_type": "client_credentials",
            "client_id": AMADEUS_API_KEY,
            "client_secret": AMADEUS_API_SECRET,
        }
        amadeus_response = requests.post(security_token, data=auth_data, headers=auth_header, verify=False)
        amadeus_json = amadeus_response.json()
        amadeus_token = amadeus_json["access_token"]
        return amadeus_token

    def get_city_code(self,city_name):
        self.city_name = city_name
        location_info = f"https://{AMADEUS_API_URL_V1}/reference-data/locations/cities"
        search_params = {
            "max": "2",
            "keyword": self.city_name,
            "include": "AIRPORTS",
        }
        response = requests.get(location_info, params=search_params, headers=self.headers, verify=False)
        response_json = response.json()
        try:
            city_code = response_json["data"][0]['iataCode']
        except KeyError:
            city_code = "N/A"
        return city_code

    def collect_flight_info(self, city_code):
        search_url = f"https://{AMADEUS_API_URL_V2}/shopping/flight-offers"
        case = []
        for day_number in range(3):
            first_date = (datetime.today() + timedelta(day_number)).strftime("%Y-%m-%d")
            last_date = (datetime.today() + timedelta(day_number + 7)).strftime("%Y-%m-%d")
            search_params = {
                "originLocationCode": ORIGIN_LOCATION,
                "destinationLocationCode": city_code,
                "departureDate": first_date,
                "returnDate": last_date,
                "adults": "1",
                "nonStop": "true",
                "currencyCode": "GBP",
                "max": "10",
            }
            response = requests.get(search_url, params=search_params, headers=self.headers, verify=False)
            if response.status_code == "429":
                response.raise_for_status()
                return []
            response_json = response.json()
            try:
                response_data = response_json["data"]
            except KeyError:
                response_data = []
            if response_data != []:
                response_data = response_json["data"]
                for flight in response_data:
                    departure_time = flight["itineraries"][0]["segments"][0]["departure"]["at"]
                    arrival_time = flight["itineraries"][1]["segments"][0]["arrival"]["at"]
                    price = flight["price"]["total"]
                    case.append({"departure_time":departure_time,"arrival_time":arrival_time,"price":price})
        return case



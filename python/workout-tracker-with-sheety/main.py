import os
import requests
from datetime import datetime as dt

NUTR_APP_ID = os.environ.get("ENV_APP_ID")
NUTR_APP_KEY = os.environ.get("ENV_APP_KEY")
NUTR_API_ADDR = "https://trackapi.nutritionix.com"
NUTR_API_EXERCISE = f"{NUTR_API_ADDR}/v2/natural/exercise"

WEIGHT_KG = os.environ.get("ENV_WEIGHT_KG")
HEIGHT_CM = os.environ.get("ENV_HEIGHT_CM")
AGE = os.environ.get("ENV_AGE")
GENDER = os.environ.get("GENDER")

SHEETY_PROJECT = "day38Workout"
SHEETY_SHEET = "workouts"
SHEETY_ENDPOINT = f"https://api.sheety.co/{SHEETY_PROJECT}/{SHEETY_SHEET}"
SHEETY_TOKEN = os.environ.get("ENV_SHEETY_TOKEN")

today_date = dt.now().strftime("%d/%m/%Y")
now_time = dt.now().strftime("%X")

headers = {
    "x-app-id": NUTR_APP_ID,
    "x-app-key": NUTR_APP_KEY,
    "Authorization": f"Basic {SHEETY_TOKEN}"
}

exercise_text = input("Tell me which exercises you did: ")

exercise_params = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE,
}

response = requests.post(url=NUTR_API_EXERCISE,json=exercise_params, headers=headers, verify=False)
response.raise_for_status()
result = response.json()

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(SHEETY_ENDPOINT, json=sheet_inputs, verify=False, headers=headers)

    print(sheet_response.text)
import requests
from datetime import datetime
import smtplib
import time

MY_LAT = -29.4618 # Your latitude
MY_LONG = -149.6748 # Your longitude
my_email = ""
my_password=""

while True:
    response = requests.get(url="http://api.open-notify.org/iss-now.json", verify=False)
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    dist_lat = abs(iss_latitude - MY_LAT)
    dist_lng = abs(iss_longitude - MY_LONG)

    #Your position is within +5 or -5 degrees of the ISS position.

    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", verify=False, params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour

    if (time_now > sunset or time_now < sunrise) and (dist_lat < 5 or dist_lng < 5):
        message = "Look Up"
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=my_password)
            connection.sendmail(from_addr=my_email,
                                to_addrs=my_email,
                                msg=f"Subject:Look Up!\n\n{message}"
                                )
    time.sleep(60)





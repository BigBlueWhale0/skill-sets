from flask import Flask, render_template
import requests
import pycountry


app = Flask(__name__)

def get_location_data():
    ip_address = requests.get('https://api64.ipify.org?format=json', verify=False).json()["ip"]
    response = requests.get(f'https://ipapi.co/{ip_address}/json/', verify=False).json()
    location_data = {
        "ip": ip_address,
        "city": response.get("city"),
        "region": response.get("region"),
        "country": response.get("country_code")
    }
    return location_data

@app.route("/")
def home():
    location_data = get_location_data()
    flag = pycountry.countries.get(alpha_2=location_data["country"]).flag
    return render_template("index.html", country=flag, city=location_data["city"])

if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask, render_template
import requests
import pycountry
import json


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

def get_news():
    with open("data/news.json") as file:
        content = json.load(file)
    return content


@app.route("/")
def home():
    location_data = get_location_data()
    flag = pycountry.countries.get(alpha_2=location_data["country"]).flag
    return render_template("index.html", country=flag, city=location_data["city"])

@app.route("/news")
def news():
    all_posts = get_news()
    print(all_posts)
    return render_template("news.html", all_posts=all_posts)

@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)
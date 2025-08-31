from bs4 import BeautifulSoup
import requests

URL = "https://appbrewery.github.io/Zillow-Clone/"

class Zillow:
    def __init__(self):
        response = requests.get(URL,verify=False)
        self.soup = BeautifulSoup(response.text, "html.parser")

    def collect_details(self):
        addresses_rows = self.soup.find_all(name="li", class_="ListItem-c11n-8-84-3-StyledListCardWrapper")
        properties = []
        for row in addresses_rows:
            address = row.find(name="address").getText().strip()
            price = row.find(name="span", class_="PropertyCardWrapper__StyledPriceLine").getText().replace("+/mo","").replace("/mo","")
            link = row.find(name="a", class_="StyledPropertyCardDataArea-anchor").get("href")
            properties.append({"address":address, "price": price, "link": link})
        return properties

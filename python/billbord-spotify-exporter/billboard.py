from bs4 import BeautifulSoup
import requests

class Billboard:
    def __init__(self):
        self.headers_billboard = {
            "USER-AGENT": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
        }
        pass

    def search_top_list(self,timestamp):
        billboard_url = f"https://www.billboard.com/charts/hot-100/{timestamp}/"
        response = requests.get(billboard_url,verify=False,headers=self.headers_billboard)
        soup = BeautifulSoup(response.text, "html.parser")
        song_names_spans = soup.select("li ul li h3")
        return [song.getText().strip() for song in song_names_spans]

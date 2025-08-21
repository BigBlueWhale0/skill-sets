import requests
import datetime

STOCK = "TSLA"
COMPANY_NAME = "tesla"

API_STOCK = ""
API_STOCK_URL = "https://www.alphavantage.co/query"
api_stock_params = {
    "apikey": API_STOCK,
    "interval": "60min",
    "symbol": STOCK,
    "function": "TIME_SERIES_INTRADAY",
}

stock_response = requests.get(API_STOCK_URL, params = api_stock_params, verify=False)

stock_data = stock_response.json()["Time Series (60min)"]

now = datetime.datetime.now()
yesterday = now.today() - datetime.timedelta(days=1)
before_yesterday = now.today() - datetime.timedelta(days=2)


yesterday_price = float(stock_data[yesterday.strftime("%Y-%m-%d %H:00:00")]["4. close"])
before_yesterday_price = float(stock_data[before_yesterday.strftime("%Y-%m-%d %H:00:00")]["1. open"])
print(abs(yesterday_price - before_yesterday_price)/before_yesterday_price)

difference = yesterday_price - before_yesterday_price

if difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"

if abs(difference)/before_yesterday_price > 0.05:
    NEWS_API_KEY = ""
    NEW_API_URL = "https://newsapi.org/v2/everything"
    api_news_params = {
        "apiKey": NEWS_API_KEY,
        "q": COMPANY_NAME,
        "page": 1,
    }
    news_response = requests.get(NEW_API_URL, params=api_news_params, verify=False)
    news_data = news_response.json()["articles"][:3]
    news_line = [f"{COMPANY_NAME}: {up_down}{difference}%\nHeadline: {article["title"]}. \nBrief: {article["description"]}" for article in news_data]


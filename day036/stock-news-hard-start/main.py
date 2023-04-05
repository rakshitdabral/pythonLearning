import requests
from twilio.rest import Client


TWILIO_END_POINT = "https://api.openweathermap.org/data/2.5/onecall"
API_ID = "0f1655ba56036959e1dafc525667a5a7"
SID = "AC62016f35a7bfac30f3ac98b26f22609b"
AUTH_TOKEN ="acb1194186ff534402dbf14ebb7a0e06"


STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API = "WGV2FMULKABWWHGY"
NEWS_API = "7d95c886194c48fa814390f56aad63b9"

parameter_stock = {
    "function": "TIME_SERIES_DAILY",
    "symbol": "TSLA",
    "interval":"1min",
    "apikey": STOCK_API
}

parameter_news= {
    "apiKey":NEWS_API,
    "qInTitle": "tesla"
}

parameter_message = {
    "lat":28.614620,
    "lon":77.03317,
    "appid": API_ID,
    "exclude": "current,minutely,daily"
}

client = Client(SID, AUTH_TOKEN)

response = requests.get(url=STOCK_ENDPOINT,params=parameter_stock)
data = response.json()["Time Series (Daily)"]
data_list = [value for (key,value) in data.items()]
yesterday_data = data.list[0]
yesterday_closing_price = yesterday_data["4. close"]

day_before_yesterday_data = data.list[1]
day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]


difference = abs(float(yesterday_closing_price)-float(day_before_yesterday_closing_price))
if difference>0:
    up_down = "📈"
else:
    up_down = "📉"

diff_per = abs((difference/yesterday_closing_price)*100)

if diff_per >5:
    response_news = requests.get(url=NEWS_ENDPOINT,params=parameter_news)
    data_news = response_news.json()["articles"]
    three_article = data_news[:3]

    formatted_article = [f"TESLA:{up_down}{diff_per}Headline:{data_news['title']}.\nBrief:{data_news['description']}" for article in three_article]

    response_sms = requests.get(url=TWILIO_END_POINT, params=parameter_message)
    response_sms.raise_for_status()
    data_sms = response_sms.json()
    message = client.messages.create(from_="+15855172194", to="+918218819454", body=f"{formatted_article}")
else:
    message = client.messages.create(from_="+15855172194", to="+918218819454", body="No change")
## STEP 1: Use https://newsapi.org/docs/endpoints/everything
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
#HINT 1: Get the closing price for yesterday and the day before yesterday. Find the positive difference between the two prices. e.g. 40 - 20 = -20, but the positive difference is 20.
#HINT 2: Work out the value of 5% of yerstday's closing stock price. 



## STEP 2: Use https://newsapi.org/docs/endpoints/everything
# Instead of printing ("Get News"), actually fetch the first 3 articles for the COMPANY_NAME. 
#HINT 1: Think about using the Python Slice Operator



## STEP 3: Use twilio.com/docs/sms/quickstart/python
# Send a separate message with each article's title and description to your phone number. 
#HINT 1: Consider using a List Comprehension.



#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""


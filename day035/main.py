import requests
from twilio.rest import Client

END_POINT = "https://api.openweathermap.org/data/2.5/onecall"
API_ID = "0f1655ba56036959e1dafc525667a5a7"
SID = "AC62016f35a7bfac30f3ac98b26f22609b"
AUTH_TOKEN ="acb1194186ff534402dbf14ebb7a0e06"

client = Client(SID,AUTH_TOKEN)

parameter = {
    "lat":28.614620,
    "lon":77.03317,
    "appid": API_ID,
    "exclude": "current,minutely,daily"
}
response = requests.get(url=END_POINT, params=parameter)
response.raise_for_status()
data = response.json()

will_rain = False

weather_slice = data["hourly"][:12]
for x in weather_slice:
    code_id = x["weather"][0]["id"]
    if int(code_id) < 700:
        will_rain = True

if will_rain:
    message = client.messages.create(from_="+15855172194", to="+918218819454",body="Carry umbrella")
else:
    message = client.messages.create(from_="+15855172194", to="+918218819454", body="No need for umbrella")
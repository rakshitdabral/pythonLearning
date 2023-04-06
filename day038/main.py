from datetime import datetime
import requests
import os

EXERCISE_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
API_KEY = os.environ["ENV_API_KEY"]
APPLICATION_ID = os.environ["ENV_APP_ID"]

AUTH_TOKEN = os.environ["ENV_AUTH_TOKEN"]

GOOGLE_SHEET_ENDPOINT = "https://api.sheety.co/19cdaf25b87b28e78c632fcb69c474ee/pythonWorkout/workouts"
GOOGLE_SHEET_API = "1V5XJc_wVofvAqI-u77Z1jJG1wD0t_5TK9qu51tCyT4U"

USER_INPUT = input("Which Exercise You Did: ")

header = {
    "x-app-id": APPLICATION_ID,
    "x-app-key":API_KEY,
    "Authorization": AUTH_TOKEN,
}


exercise_config = {
    "query": USER_INPUT,
    "gender": "male",
    "weight_kg": "68.25",
    "height_cm": "167.64",
    "age":"19",
}

response = requests.post(url=EXERCISE_ENDPOINT, json=exercise_config, headers=header)
result = response.json()

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_config = {
        "workout" : {
            "date" : today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
         }
    }

sheet_response = requests.post(url=GOOGLE_SHEET_ENDPOINT, json=sheet_config)
print(sheet_response.text)



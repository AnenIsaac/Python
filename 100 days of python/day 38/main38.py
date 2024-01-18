import requests
from datetime import datetime

APPID = "cfc758ec"
APIKEYS = "ae7b0c777a53bbb111e8e6bce7c7cfc5"
endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
endpoint_calories = "ae7b0c777a53bbb111e8e6bce7c7cfc5"
sheets_url ='https://api.sheety.co/db576b61a317675d114004c8294a6961/workouts/workouts'

user_weight = 74
user_height = 183
user_age = 20
user_input = input("what did you do today?")

header = {
    "x-app-id" : APPID, 
    "x-app-key" : APIKEYS,
    "Content-Type": "application/json"
}
 
params = {
    "query": user_input,  # Include the user's input as the "query" parameter
    "weight_kg": user_weight,
    "height_cm": user_height,
    "age": user_age,
}
# test_data = {
#   "workout": {
# 	"date": "Syed K",
# 	"time": "syed@gmail.com", 
#     "exercise": 'Running', 
#     "duration": "22", 
#     "calories":'130'
#   }
# } 
response = requests.post(url=endpoint, headers=header, json=params)
data = response.json()
list_of_exercise = data['exercises']
# response = requests.post(url=sheets_url, json = test_data)
print(response.text)
for item in list_of_exercise:
  sheets_data = {
    "workout": {
      "date": f"{datetime.now().strftime('%d/%m/%y')}",
      "time": f"{datetime.now().strftime('%H:%M:%S')}",
      "exercise": item['name'].title(),
      "duration": round(item['duration_min']),
      "calories":round(item['nf_calories']),
    }
    }
  response = requests.post(url=sheets_url, json = sheets_data)
  print(response.text)

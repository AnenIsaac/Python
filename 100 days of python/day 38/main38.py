import requests

APPID = "cfc758ec"
APIKEYS = "ae7b0c777a53bbb111e8e6bce7c7cfc5"
endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
endpoint_calories = "ae7b0c777a53bbb111e8e6bce7c7cfc5"
sheets_url ='https://api.sheety.co/db576b61a317675d114004c8294a6961/myWorkouts/workouts'

user_weight = 74
user_height = 183
user_age = 20
user_input = input("what did you do today?")

header = {
    "x-app-id" : APPID, 
    "x-app-key" : APIKEYS,
}
 
params = {
    "query": user_input,  # Include the user's input as the "query" parameter
    "weight_kg": user_weight,
    "height_cm": user_height,
    "age": user_age,
}

response = requests.post(url=endpoint, headers=header, json=params)
print(response.text)

# it starts here
print(f"Nutritionix API call: \n {result} \n")

# Adding date and time
today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

# Sheety Project API. Check your Google sheet name and Sheety endpoint
GOOGLE_SHEET_NAME = "workout"
sheet_endpoint = os.environ[
    "ENV_SHEETY_ENDPOINT"]

# Sheety API Call & Authentication
for exercise in result["exercises"]:
    sheet_inputs = {
        GOOGLE_SHEET_NAME: {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    # Sheety Authentication Option 1: No Auth
    """
    sheet_response = requests.post(sheet_endpoint, json=sheet_inputs)
    """

    # Sheety Authentication Option 2: Basic Auth
    sheet_response = requests.post(
        sheet_endpoint,
        json=sheet_inputs,
        auth=(
            os.environ["ENV_SHEETY_USERNAME"],
            os.environ["ENV_SHEETY_PASSWORD"],
        )
    )

    # Sheety Authentication Option 3: Bearer Token
    """
    bearer_headers = {
        "Authorization": f"Bearer {os.environ['ENV_SHEETY_TOKEN']}"
    }
    sheet_response = requests.post(
        sheet_endpoint,
        json=sheet_inputs,
        headers=bearer_headers
    )    
    """
    print(f"Sheety Response: \n {sheet_response.text}")
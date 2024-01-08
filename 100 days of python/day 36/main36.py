import requests
from datetime import datetime

# replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
url = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=60min&apikey=GSVF0FMNWZCKBRJ6'
r = requests.get(url)
data = r.json()
time_series = data.get('Time Series (60min)', {})
last_element = list(time_series.items())[16][-1] if time_series else None
closing_price = last_element['4. close']
print(last_element)
# print(closing_price)
# current_date = datetime.now().date()
# formatted_date = current_date.strftime("%Y-%m-%d")
# Closing_time = f"{current_date} 19:00:00"
# current_day_of_week = datetime.now().weekday()
# is_weekend = current_date in [5,6]:
# if is_weekend:
    

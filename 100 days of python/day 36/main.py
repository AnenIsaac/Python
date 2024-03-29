import requests
from twilio.rest import Client

TWILIO_SID = "AC9de5760c324ae7f89dab730976d99200"
TWILIO_AUTH = "6e65fbf3cef06a1ffc0a9e965690e90a"
STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
STOCK_API_KEY = "GSVF0FMNWZCKBRJ6"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_API_KEY = "9151d9056ed14eef8160eeb30ef99dbd"

    ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

#TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]
url = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=60min&apikey=GSVF0FMNWZCKBRJ6'
r = requests.get(url)
data = r.json()
time_series = data.get('Time Series (60min)', {})
yesterday_last_element = list(time_series.items())[0][-1] if time_series else None
yesterday_closing_price = float(yesterday_last_element['4. close'])
print(f"yesterday closing price = {yesterday_closing_price}")
      
#TODO 2. - Get the day before yesterday's closing stock price
before_yesterday_last_element = list(time_series.items())[16][-1] if time_series else None
before_yesterday_closing_price = float(before_yesterday_last_element['4. close'])
print(f"before yesterday closing price = {before_yesterday_closing_price}")
#TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp
Positive_difference = before_yesterday_closing_price - yesterday_closing_price
print(f"positive difference = {Positive_difference}")
#TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
percentage_difference = (Positive_difference / before_yesterday_closing_price) * 100
print(f"percentage difference = {percentage_difference}")
#TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").
if percentage_difference > 5 or percentage_difference < -5:
    print("Get News")
else:
    print("Nothing special has happened")
    ## STEP 2: https://newsapi.org/ 
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

#TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.
updown = None
if percentage_difference > 0:
    updown = "🔺"
else:
    updown = "🔻"
    
if abs(percentage_difference) > 0:
    news_params = {
        "apikey" : NEWS_API_KEY,
        "qInTitle" : COMPANY_NAME,
    }

    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    articles = news_response.json()["articles"]
    
#TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation
    three_articles = articles[:3]
    print(three_articles)

    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number. 

#TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.
print("\n")
print("\n")
print("\n")
formatted_article = [f"{STOCK_NAME}: {updown} {round(percentage_difference, 2)}%\nHeadline: {article['title']}. \nBrief: {article['description']}" for article in three_articles]
print(formatted_article)
#TODO 9. - Send each article as a separate message via Twilio. 

client = Client(TWILIO_SID, TWILIO_AUTH)

for article in formatted_article:
    message = client.messages.create(
        body=article,
        from_= "+12056905776",
        to="+255763860354"
    )
#Optional TODO: Format the message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""


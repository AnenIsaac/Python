import smtplib
import datetime as dt 
import random

MY_EMAIL = "kelvinisshayo@gmail.com"
PASSWORD = "macmuykehevhutvh"
now = dt.datetime.now()
weekday = now.weekday()
print(weekday)
if weekday == 4:
    with open("quotes.txt") as file:
        all_quotes = file.readlines()
        quote = random.choice(all_quotes)
        
    print(quote)
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, PASSWORD)
        connection.sendmail(MY_EMAIL, "anenbisaaclaseko@gmail.com", msg= f"Subject: Your daily dose of motivation\n\n{quote}")
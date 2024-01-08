import smtplib

# Host = "smtp.gmail.com"
# Port: 587
# Encryption: TLS
# User: yourgmail@gmail.com
# Password: xmmpzcxmfhwyzdja

my_email = "kelvinisshayo@gmail.com"
password = "gimymduqevnjuury"

with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email, 
        to_addrs="anenbisaaclaseko@gmail.com", 
        msg="Subject: A hello message\n\nI wanted to say hello. This message was sent to you through python!!!"
        )
 
# import datetime as dt  

# now = dt.datetime.now()
# year = now.weekday()

# print(year)

# dob = dt.datetime(year=2003, month=9, day=6)
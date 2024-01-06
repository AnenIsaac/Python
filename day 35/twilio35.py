from twilio.rest import Client

account_sid = 'AC9de5760c324ae7f89dab730976d99200'
auth_token = '6a0034540a919565d760677076a86f1c'
client = Client(account_sid, auth_token)

message = client.messages.create(
  from_='+12056905776',
  body="Hey Anen, it seems like it might rain today. Make sure to bring an umbrella!",
  to='+255763860354'
)

print(message.sid)
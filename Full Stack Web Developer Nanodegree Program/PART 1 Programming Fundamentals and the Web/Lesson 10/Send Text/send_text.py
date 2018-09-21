# Sending an SMS using the Twilio API
from twilio.rest import Client

# put your own credentials here
account_sid = "AC67e5dd6bb1d57c59497be61d6e556eb9"
auth_token = "bcd6240151648730bd99372970821ac7"

client = Client(account_sid, auth_token)
message = client.messages.create(
  to="+12268202393",
  from_="+16476914136",
  body="Twilio test message")
print message.sid

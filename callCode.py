# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client

# Set environment variables for your credentials
# Read more at http://twil.io/secure

account_sid = "AC7d292b17e3788c71c5b8004c8632fc0f"
auth_token = "f52b53f0218be47856ea6d7bce762325"
client = Client(account_sid, auth_token)

call = client.calls.create(
  url="http://demo.twilio.com/docs/voice.xml",
  to="+18582509640",
  from_="+18332477947"
)

print(call.sid)
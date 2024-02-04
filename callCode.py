# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client

# Set environment variables for your credentials
# Read more at http://twil.io/secure

account_sid = "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
auth_token = "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
client = Client(account_sid, auth_token)

call = client.calls.create(
  url="http://demo.twilio.com/docs/voice.xml",
  to="+1123456789",
  from_="+1123456789"
)

print(call.sid)

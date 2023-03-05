import os
from twilio.rest import Client
import random

# Your Twilio account SID and auth token
account_sid = 'AC02d04544f9a7051d87270ee723100387'
auth_token = '22b7c906971e450236481031b0847955'

# Create a new Twilio client object
client = Client(account_sid, auth_token)

# The phone number to send the OTP code to
to_phone_number = '+919354023059'  # Replace with the actual phone number

# Generate a random 6-digit OTP code (you can customize this to your needs)
length=5
def generate_random_string(length):
     digits = "0123456789"
     a= ''.join(random.choice(digits) for i in range(length))
     print(a)
     return a

otp_code = generate_random_string(5)

# The message to send with the OTP code
message = f'This is otp for neighshop  {otp_code} DO NOT SHARE IT WITH ANYONE'

# The Twilio phone number to use as the sender
from_phone_number = '+12762779220'

# Use the Twilio client to send the SMS message with the OTP code
message = client.messages.create(
    body=message,
    from_=from_phone_number,
    to=to_phone_number
)

# Print the Twilio message ID to confirm that the message was sent successfully
print(f'Message sent with ID: {message.sid}')

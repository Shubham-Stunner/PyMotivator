from twilio.rest import Client
from config import account_sid,auth_token,phone_number

def set_twilio_connection(account_sid, auth_token):
    client = Client(account_sid, auth_token)
    return client

def send_whatsapp_text(client,quotes):
    message = client.messages.create(
    from_='whatsapp:+14155238886',
    body=quotes,
    to='whatsapp:+917991141260'
    )

    return message.sid

client = set_twilio_connection(account_sid,auth_token)
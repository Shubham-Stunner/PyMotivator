#extracting quotes form API 
import requests
from twilio_conn import send_whatsapp_text, client  # Assuming you have defined these somewhere

def get_quotes_by_category(category):
    api_url = 'https://api.api-ninjas.com/v1/quotes?category={}'.format(category)
    api_key = 'lF2zJXZ5za9Zrr6CF4TEsg==4okhYQ3zybsFCUY2'

    response = requests.get(api_url, headers={'X-Api-Key': api_key})

    if response.status_code == requests.codes.ok:
        data = response.json()
        status = response.status_code
        if status == 200:
            quotes = [quote['quote'] for quote in data]
            return quotes  # Return quotes here
        elif status == 400:
            quotes = [quote['error'] for error in data]
            return quotes  # Return quotes here
    else:
        print("Error:", response.status_code, response.text)

# Example usage:
category = 'life'
quotes = get_quotes_by_category(category)  # Capture returned quotes
send_whatsapp_text(client, quotes)  # Assuming this function works with the quotes received


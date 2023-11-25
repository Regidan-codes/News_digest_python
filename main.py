import requests
from send_email import send_email

api_key = "e5959d92dac14f1da70f50b3255ef416"
url = ("https://newsapi.org/v2/everything?q=tesla&from=2023-10-25&sortBy=publishedAt&apiKey"
       "=e5959d92dac14f1da70f50b3255ef416")

# Make request
response = requests.get(url)

# Get a dictionary
content = response.json()

# Iterate through a dictionary
body = ""
for item in content['articles']:
    if item['title'] is not None:
        body += item['title'] + "\n" + item['description'] + 2*"\n"

body = body.encode('utf-8')
send_email(message=body)

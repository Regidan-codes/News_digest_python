import requests
from send_email import send_email

topic = "tesla"
api_key = "e5959d92dac14f1da70f50b3255ef416"
url = ("https://newsapi.org/v2/everything?"
       "domains=techcrunch.com,thenextweb.com,inverse.com&"
       "sortBy=popularity&"
       "apiKey=e5959d92dac14f1da70f50b3255ef416&"
       "language=en")

# Make request
response = requests.get(url)

# Get a dictionary
content = response.json()

# Iterate through a dictionary
body = ""
for item in content['articles'][:20]:
    if item['title'] and item['description'] is not None:
        body += "Subject: Today's News" \
                 + "\n" + item['title'] \
                 + "\n" + item['description'] + "\n" + item['url'] + 2 * "\n"

body = body.encode('utf-8')
send_email(message=body)

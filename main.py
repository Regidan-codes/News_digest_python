import requests

api_key = "e5959d92dac14f1da70f50b3255ef416"
url = ("https://newsapi.org/v2/everything?q=tesla&from=2023-10-25&sortBy=publishedAt&apiKey"
       "=e5959d92dac14f1da70f50b3255ef416")

# Make request
response = requests.get(url)
content = response.json()
for item in content['articles']:
    print(item['title'])
    print(item['description'])

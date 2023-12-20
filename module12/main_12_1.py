import requests

url = "https://api.chucknorris.io/jokes/random"

querystring = {"apikey": "873dbe322aea47f89dcf729dcc8f60e8"}

response = requests.get(url)

str = response.json()
print(str['value'])

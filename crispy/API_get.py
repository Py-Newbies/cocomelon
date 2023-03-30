import requests
from pprint import pprint

URL = "https://api.thedogapi.com/v1/breeds"

response = requests.get(URL)

data = response.json()

pprint(data)

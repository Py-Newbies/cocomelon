import requests
from pprint import pprint

# URL = "https://api.thedogapi.com/v1/breeds"

BASE_URL = "https://api.thedogapi.com/{}"

headers = {'Content-Type': 'application/json',
           'x-api-key': 'live_RAbjMzLty32bWKc54yiImvD47xQ3NMCwKE7YhvH5cswNHhui3FXKx2ShCf4QDvBf'}

data = {
    "image_id": "GAmy2bg8G",
    "sub_id": "my-user-1232",
    "value": -1
}
response = requests.post(BASE_URL.format("v1/votes"), headers=headers, json=data)

# requests.get(BASE_URL.format("v1/votes?sub_id=my-user-1232"), headers=headers)

data = response.json()

pprint(data)




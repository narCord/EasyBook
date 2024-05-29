import requests
import json

headers = {
    'User-Agent': 'OrbisTertius/1.0 (narciso.cordeiro18@gmail.com)'
}
query = ''
url = f'https://openlibrary.org/search.json?q={query}'

response = requests.get(url, headers=headers)
response_json = response.json()
print(response_json['docs'][0])
#for key in response_json:
#    print(response_json[key])

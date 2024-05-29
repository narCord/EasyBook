import requests
import json

class api_manager:
    print('')

headers = {
    'User-Agent': 'OrbisTertius/1.0 (narciso.cordeiro18@gmail.com)'
}
query = 'outer dark'
url = f'https://openlibrary.org/search.json?q={query}'

response = requests.get(url, headers=headers)
json_data = response.json()


print(json_data)

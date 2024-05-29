import requests

headers = {
    'User-Agent': 'OrbisTertius/1.0 (narciso.cordeiro18@gmail.com)'
}
query = ''
url = f'https://openlibrary.org/search.json?q={query}'

response = requests.get(url, headers=headers)
print(response.json())

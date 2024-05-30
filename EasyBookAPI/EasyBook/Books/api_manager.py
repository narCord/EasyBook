import requests


class ApiManager:
    headers = {
        'User-Agent': 'OrbisTertius/1.0 (narciso.cordeiro18@gmail.com)'
    }

    author_name = ''
    first_publish_year = ''
    title = ''
    subject = ''
    first_sentence = ''

    subject_list = ['Fiction', 'History', 'Drama', 'Memoir', 'Literary criticism', 'Poetry', 'Non-fiction']

    def book_search(self, query):
        url = f'https://openlibrary.org/search.json?q={query}&limit=1'
        response = requests.get(url, headers=self.headers)
        json_data = response.json().get('docs')[0]

        self.author_name = json_data.get('author_name')[0]
        self.first_publish_year = json_data.get('first_publish_year')
        self.title = json_data.get('title')
        try:
           self.subject = self.subject_selection(json_data.get('subject'))
        except TypeError:
            self.subject = 'Undefined'
        try:
            self.first_sentence = json_data.get('first_sentence')[0]
        except TypeError:
            self.first_sentence = 'Undefined'

    def subject_selection(self, queried_book_subject_list):
        for item in queried_book_subject_list:
            if item in self.subject_list:
                return item

        return 'Undefined'

'''
api_call = ApiManager()
api_call.book_search('the lord of the rings')
print(api_call.author_name)
print(api_call.first_publish_year)
print(api_call.title)
print(api_call.subject)
print(api_call.first_sentence)
'''

import json
from json import encoder


class JsonBuilder:
    def __init__(self, author_name, first_publish_year, title, subject, first_sentence):
        self.author_name = author_name
        self.first_publish_year = first_publish_year
        self.title = title
        self.subject = subject
        self.first_sentence = first_sentence

    def to_json(self):
        data_array = {
            'author_name': self.author_name,
            'first_publish_year': self.first_publish_year,
            'title': self.title,
            'subject': self.subject,
            'first_sentece': self.first_sentence
        }

        return json.dumps(data_array, indent=4)

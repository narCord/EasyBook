import json

from django.http import JsonResponse

from .api_manager import ApiManager
from .json_builder import JsonBuilder


def book_search(request):
    query = request.GET.get('q')
    api_test = ApiManager()
    api_test.book_search(query)

    builder = JsonBuilder(api_test.author_name, api_test.first_publish_year, api_test.title, api_test.subject,
                          api_test.first_sentence)
    json_response = json.loads(builder.to_json())

    return JsonResponse(json_response, status=200, safe=False)

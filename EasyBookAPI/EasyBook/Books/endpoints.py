import json
from django.http import JsonResponse, HttpResponse
from rest_framework.permissions import IsAuthenticated

from .api_manager import ApiManager
from .json_builder import JsonBuilder
from .models import Book, BooksReadByUser, BooksAbandonedByUser, BooksToBeReadByUser, User


def book_search(request):
    query = request.GET.get('q')
    api_test = ApiManager()
    api_test.book_search(query)

    builder = JsonBuilder(api_test.author_name, api_test.first_publish_year, api_test.title, api_test.subject,
                          api_test.first_sentence)
    json_response = json.loads(builder.to_json())

    # new_book = Book(author_name=api_test.author_name,
    #                 first_publish_year=api_test.first_publish_year,
    #                 title=api_test.title,
    #                 subject=api_test.subject,
    #                 first_sentence=api_test.first_sentence)
    #
    # new_book.save()

    return JsonResponse(json_response, status=200, safe=False)


def testing(request, HttpRequest):
    request = HttpRequest()
    # user = Book.objects.get(pk=1)
    # print(user.title)
    # print(user.first_publish_year)
    # print(user.author_name)
    # print(user.subject)
    # print(user.first_sentence)

    permission = IsAuthenticated()
    if permission.has_permission(None, request):
        return JsonResponse({'MENSAJE': 'acceso concedido'}, status=200)
    else:
        return JsonResponse({'mensaje': 'sin permiso'}, status=400)


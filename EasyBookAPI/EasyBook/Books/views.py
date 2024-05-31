from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated
import json
from django.http import JsonResponse, HttpResponse
from rest_framework.permissions import IsAuthenticated
from .api_manager import ApiManager
from .json_builder import JsonBuilder
from .models import Book, BooksReadByUser, BooksAbandonedByUser, BooksToBeReadByUser, User


class CreateUserView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


#http://127.0.0.1:8000/api/logout/
#Postman Headers: Authorization, Bearer <access token>
#body {"refresh": "<refresh token>"}
class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            refresh_token = request.data.get('refresh')
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({'message': 'Logged out succesfully'}, status=200)
        except Exception as e:
            return Response({'error': str(e)}, status=400)


class AddToReadList(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request):
        query = request.GET.get('q')
        check_and_add_book(query)

        request_user = request.user
        # request.data.get('rating')
        # request.data.get('note')
        book_read, created = BooksReadByUser.objects.update_or_create(
            user=request_user,
            book=Book.objects.get(title__iexact=query),
            rating=request.data.get('rating'),
            note=request.data.get('note')
        )
        return JsonResponse({'status': 'exito'}, status=200)

    # def get(self, request):
    #     user = request.user
    #     username = user.username
    #     password = user.password
    #     return JsonResponse({f'{username}': f'{password}'}, status=200)


class AddToAbandonedList(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request):
        query = request.GET.get('q')


class AddToToBeReadList(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request):
        query = request.GET.get('q')


class RemoveFromReadList(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request):
        query = request.GET.get('q')


class RemoveFromAbandonedList(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request):
        query = request.GET.get('q')


class RemoveFromToBeReadList(APIView):
    permission_classes = [IsAuthenticated]
    def put(self, request):
        query = request.GET.get('q')


class TestingClass(APIView):
    def get(self, request):
        query = request.GET.get('q')


class BookSearch(APIView):
    def get(self, request):
        query = request.GET.get('q')
        api_test = ApiManager()
        api_test.book_search(query)

        builder = JsonBuilder(api_test.author_name, api_test.first_publish_year, api_test.title, api_test.subject,
                              api_test.first_sentence)
        json_response = json.loads(builder.to_json())

        return JsonResponse(json_response, status=200, safe=False)


class SearchAndAddBookToDatabase(APIView):
    def get(self, request):
        query = request.GET.get('q')

        json_response = check_and_add_book(query)

        return JsonResponse(json_response, status=200, safe=False)


def check_and_add_book(query):
    if Book.objects.filter(title__iexact=query).exists():
        book = Book.objects.get(title__iexact=query)
        return {'status': 'The book already exists in the database',
                'book': {
                    'author_name': book.author_name,
                    'first_publish_year': book.first_publish_year,
                    'title': book.title,
                    'subject': book.subject,
                    'first_sentence': book.first_sentence
                    }
                }
    else:
        #
        api_test = ApiManager()
        api_test.book_search(query)
        builder = JsonBuilder(api_test.author_name,
                              api_test.first_publish_year,
                              api_test.title,
                              api_test.subject,
                              api_test.first_sentence)
        json_response = json.loads(builder.to_json())
        new_book = Book(author_name=api_test.author_name,
                        first_publish_year=api_test.first_publish_year,
                        title=api_test.title,
                        subject=api_test.subject,
                        first_sentence=api_test.first_sentence)
        new_book.save()
        return json_response

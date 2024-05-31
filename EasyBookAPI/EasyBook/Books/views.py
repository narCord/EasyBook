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

    def get(self, request):
        user = request.user
        username = user.username
        password = user.password
        return JsonResponse({f'{username}': f'{password}'}, status=200)


class AddToAbandonedList(APIView):
    permission_classes = [IsAuthenticated]
    pass


class AddToToBeReadList(APIView):
    permission_classes = [IsAuthenticated]
    pass


class RemoveFromReadList(APIView):
    permission_classes = [IsAuthenticated]
    pass


class RemoveFromAbandonedList(APIView):
    permission_classes = [IsAuthenticated]
    pass


class RemoveFromToBeReadList(APIView):
    permission_classes = [IsAuthenticated]
    pass


class TestingClass(APIView):
    def get(self, request):
        pass


class BookSearch(APIView):
    def get(self, request):
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

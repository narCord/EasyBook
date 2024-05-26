from django.shortcuts import render
from django.http import HttpResponse
from .serializers import UserRegistrationSerializer
from django.contrib.auth.models import User
from rest_framework import viewsets

# Create your views here.
def index(request):
    return HttpResponse('Hola estas en la pagina principal de EasyBook')

class UserRegistrationViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer

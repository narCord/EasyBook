from django.urls import path, include
from . import views
from .views import CreateUserView

urlpatterns = [
    path('create-user/', CreateUserView.as_view(), name='create-user')
]
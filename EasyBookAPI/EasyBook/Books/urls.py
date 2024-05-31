from django.urls import path
from .views import *
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from . import test

urlpatterns = [
    path('create-user/', CreateUserView.as_view(), name='create-user'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('user/add/read/', AddToReadList.as_view(), name='add_to_read'),
    path('user/add/abandoned/', AddToAbandonedList.as_view(), name='add_to_abandoned'),
    path('user/add/toberead/', AddToToBeReadList.as_view(), name='add_to_toberead'),
    path('user/remove/read/', RemoveFromReadList.as_view(), name='remove_from_read'),
    path('user/remove/abandoned/', RemoveFromAbandonedList.as_view(), name='remove_from_abandoned'),
    path('user/remove/toberead/', RemoveFromToBeReadList.as_view(), name='remove_from_toberead'),
    path('search/', BookSearch.as_view(), name='book_search'),
    path('add/', SearchAndAddBookToDatabase.as_view(), name='search_and_add_book'),
    path('testing/', TestingClass.as_view(), name='testing'),
    path('cancer/', test.cancer),
]

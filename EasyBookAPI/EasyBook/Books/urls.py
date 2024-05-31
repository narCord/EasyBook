from django.urls import path
from .views import *
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('create-user/', CreateUserView.as_view(), name='create-user'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('jaja/', AddToReadList.as_view(), name='add_to_read'),
    path('search/', BookSearch.as_view(), name='book_search'),
    path('testing/', TestingClass.as_view(), name='testing'),
]

from django.urls import path, include
from . import views, endpoints
from .views import CreateUserView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
import rest_framework.views

urlpatterns = [
    path('create-user/', CreateUserView.as_view(), name='create-user'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('search/', endpoints.book_search),
#    path('test/<int:testId>', endpoints.test),
]
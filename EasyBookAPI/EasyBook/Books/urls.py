from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from .views import UserRegistrationViewSet

router = DefaultRouter()
router.register(r'register', UserRegistrationViewSet, basename='user_registration')

urlpatterns = [
    path('', include(router.urls))
]
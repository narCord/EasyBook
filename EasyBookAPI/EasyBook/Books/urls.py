from django.urls import path
from . import views, endpoints

urlpatterns = [
    path('', views.index, name='index'),
    path('test/', endpoints.test2),
    path('test/<int:testId>', endpoints.test),

]
from django.contrib import admin
from django.urls import path, include 
from .views import SignUpView, index, UserListCreate

urlpatterns = [
    path('signup', SignUpView.as_view(), name='signup'),
    path('', index, name='index'),
    path('api/', UserListCreate.as_view()),

]
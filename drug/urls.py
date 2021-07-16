from django.contrib import admin
from django.urls import path
from .views import DrugCreateAPI

urlpatterns = [
    path('', DrugCreateAPI.as_view()),
]
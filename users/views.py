from rest_framework import generics
from .models import CustomUser
from .serializers import UserSerializer
from .forms import CustomUserCreationForm
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.template import loader
from django.urls import reverse_lazy
from django.views import generic

class SignUpView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('')
    template_name = 'users/signup.html'
    success_message = "Your profile was created successfully"

def index(request):
    pass 

class UserListCreate(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

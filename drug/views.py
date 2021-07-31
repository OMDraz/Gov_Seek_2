from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Drug
from django.http import Http404
from .serializers import DrugSerializer
from rest_framework import status
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage

class DrugList(generics.ListCreateAPIView):
    queryset = Drug.objects.all()
    serializer_class = DrugSerializer


class DrugDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Drug.objects.all()
    serializer_class = DrugSerializer

def upload(request):
    if request.method == "POST":
        uploaded_file = request.FILES['document']
        print(uploaded_file.name)
        print(uploaded_file.size)
    return render(request, 'upload.html')
    
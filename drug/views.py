from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Drug
from django.http import Http404
from .serializers import DrugSerializer
from rest_framework import status

class DrugList(generics.ListCreateAPIView):
    queryset = Drug.objects.all()
    serializer_class = DrugSerializer


class DrugDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Drug.objects.all()
    serializer_class = DrugSerializer

    
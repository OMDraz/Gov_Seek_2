import json
from rest_framework.views import APIView
from rest_framework.response import Response
from urllib.request import urlopen
from .models import Drug
from .serializers import DrugSerializer
from rest_framework import generics


class UserListCreate(generics.ListCreateAPIView):
    queryset = Drug.objects.all()
    serializer_class = DrugSerializer

    def list(self, reuqest):
        queryset = self.get_queryset()
        serializer = DrugSerializer(queryset, many=True)
        return Response(serializer.data)
import json
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from urllib.request import urlopen
from .models import Drug
from .serializers import DrugSerializer, ActiveIngredientsSerializer, OpenFDASerializer, PackagingSerializer
from rest_framework import generics, status
from django.db import transaction

class DrugCreateAPI(CreateAPIView):
    queryset = Drug.objects.all()
    serializer_class = DrugSerializer

    # We skip perform_create
    def create(self, request, *args, **kwargs):
        try:
            active_ingredients = request.data.pop('active_ingredients')
            packaging = request.data.pop('packaging')
            openfda = request.data.pop('openfda')
        except KeyError:
            return Response({}, status=status.HTTP_400_BAD_REQUEST)
        print(request.data)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        with transaction.atomic():
            instance = serializer.save()
            # Validate each item
            for item in active_ingredients:
                print(item)
                s = ActiveIngredientsSerializer(data=item)
                s.is_valid(raise_exception=True)
                s.save(campaign=instance)
            for item in packaging:
                print(item)
                s = PackagingSerializer(data=item)
                s.is_valid(raise_exception=True)
                s.save(campaign=instance)
            for item in openfda:
                s = OpenFDASerializer(data=item)
                s.is_valid(raise_exception=True)
                s.save(campaign=instance)
        headers = self.get_success_headers(serializer.data)
        serializer.data['active_ingredients'] = active_ingredients
        serializer.data['packaging'] = packaging
        serializer.data['openfda'] = openfda
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    
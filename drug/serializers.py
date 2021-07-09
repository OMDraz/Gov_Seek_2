from .models import Drug, Packaging, ActiveIngredients, OpenFDA
from rest_framework import serializers 
from .utils import get_if_exists 

class PackagingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drug
        fields = '__all__'

class ActiveIngredientsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drug
        fields = '__all__'

class OpenFDASerializer(serializers.ModelSerializer):
    class Meta:
        model = Drug
        fields = '__all__'

class DrugSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drug
        fields = '__all__'
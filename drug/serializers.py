from rest_framework.fields import CharField, DictField
from .models import Drug, Packaging, ActiveIngredients, OpenFDA
from rest_framework import serializers 
from .utils import get_if_exists 

class PackagingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Packaging
        fields = '__all__'

class ActiveIngredientsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActiveIngredients
        fields = '__all__'

class OpenFDASerializer(serializers.ModelSerializer):
    class Meta:
        model = OpenFDA
        fields = '__all__'

class DrugSerializer(serializers.ModelSerializer):
    openfda = OpenFDASerializer()
    packaging = PackagingSerializer(many=True)
    active_ingredients = ActiveIngredientsSerializer(many=True)

    pharm_class = serializers.ListField(
            child=serializers.CharField(),
            allow_empty=True
        )
    route = serializers.ListField(
            child=serializers.CharField(),
            allow_empty=True
        )
    
    openfda_data = serializers.ListField(
            child=serializers.CharField(),
            allow_empty=True
        )



    class Meta:
        model = Drug
        fields = '__all__'
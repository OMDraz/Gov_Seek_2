from .models import Drug, Packaging, ActiveIngredients, OpenFDA
from rest_framework import serializers 

##Added some comments
class PackagingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Packaging
        fields = "__all__"

class OpenFDASerializer(serializers.ModelSerializer):
    class Meta:
        model = OpenFDA
        fields = "__all__"

class ActiveIngredientsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActiveIngredients
        fields = "__all__"
    

class DrugSerializer(serializers.ModelSerializer):
    active_ingredients = ActiveIngredientsSerializer(many=True)
    packaging = PackagingSerializer(many=True)
    openfda = OpenFDASerializer()


    class Meta:
        model = Drug 
        fields = "__all__"
    
    def create(self, validated_data):
        active_ingredient_data = validated_data.pop('active_ingredients')
        packaging_data = validated_data.pop('packaging')
        openfda_data = validated_data.pop('openfda')

        drug = Drug.objects.create(**validated_data)

        for data in active_ingredient_data:
            ActiveIngredients.objects.create(drug=drug, **data)
        for data in packaging_data:
            Packaging.objects.create(drug=drug, **data)
        for data in openfda_data:
            OpenFDA.objects.create(drug=drug, **data)
        return drug
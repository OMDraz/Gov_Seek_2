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
    class Meta:
        model = Drug
        fields = '__all__'
        extra_kwargs = {'openfda': {'required': False}}

    def create(self, validated_data):
        openfda_data = validated_data.pop('openfda')
        return openfda_data
        # packaging_data = validated_data.pop('packaging')
        # active_ingredients_data = validated_data.pop('active_ingredients')
        # drug = Drug.objects.create(**validated_data)

        # for openfda_datas in openfda_data:
        #     OpenFDA.objects.create(drug=drug, **openfda_datas)
        # for active_ingredient_data in active_ingredients_data:
        #     ActiveIngredients.objects.create(drug=drug, **active_ingredient_data)
        # for packaging_datas in packaging_data:
        #     Packaging.objects.create(drug=drug, **packaging_datas)
        # return drug
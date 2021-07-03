from .models import Drug, Packaging, ActiveIngredients, OpenFDA
from rest_framework import serializers 

class PackagingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Packaging
        fields = ['drug','package_ndc','description','marketing_start_date','sample',]

class OpenFDASerializer(serializers.ModelSerializer):
    class Meta:
        model = OpenFDA
        fields = ['drug','manufacturer_name','rxcui','unii','spl_set_id',]

class ActiveIngredientsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActiveIngredients
        fields = ['drug','name','strength']
    

class DrugSerializer(serializers.ModelSerializer):
    active_ingredients = ActiveIngredientsSerializer(many=True)
    packaging = PackagingSerializer(many=True)
    openfda = serializers.ListField()


    class Meta:
        model = Drug 
        fields = ['product_ndc','generic_name','labeler_name','brand_name','active_ingredients','finished','packaging','listing_expiration_date','openfda','marketing_category','dosage_form','spl_id','product_type','marketing_start_date','product_id','application_number','brand_name_base','pharm_class',]
    
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
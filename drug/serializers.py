from .models import Drug, Packaging, ActiveIngredients, OpenFDA
from rest_framework import serializers 
from .utils import get_if_exists 

# just some small changes so I can push to git 

class DrugSerializer(serializers.Serializer):
    """
    Custom serializer for drugs
    """

    drug_id = serializers.CharField(
        max_length=50, 
    )
    product_ndc = serializers.CharField(
        max_length=50, 
    )
    generic_name = serializers.CharField(
        max_length=50, 
    )
    labeler_name = serializers.CharField(
        max_length=50, 
    )
    brand_name = serializers.CharField(
        max_length=50, 
    )
    active_ingredients = serializers.ListField(
        child=serializers.CharField()
    )
    finished = serializers.CharField(
        max_length=50, 
    )
    packaging = serializers.ListField(
        child=serializers.CharField()
    )
    listing_expiration_date = serializers.CharField(
        max_length=50, 
    )
    openfda = serializers.ListField(
        child=serializers.CharField()
    )

    def create(self, validated_data):
        return Drug(**validated_data)

    # def update(self, instance, validated_data):
    #     """TODO: remove explicit update behavior and shift to a back
    #     up and create new entry pattern. Seems like a better data integrity
    #     approach
    #     requires a new field for managing state of record (eg.'deleted')"""

    #     self.restaurant_id = validated_data.get(
    #         'restaurant_id', instance.restaurant_id)
    #     self.name = validated_data.get('name', instance.name)
    #     self.street_address = validated_data.get(
    #         'street_address', instance.street_address)
    #     self.city = validated_data.get('city', instance.city)
    #     self.state = validated_data.get('state', instance.state)
    #     self.postal_code = validated_data.get(
    #         'postal_code', instance.postal_code)
    #     instance.save()
    #     return instance





class PackagingSerializer(serializers.ModelSerializer):
    drug = DrugSerializer() 

    class Meta:
        model = Packaging
        fields = ['drug','package_ndc','description','marketing_start_date','sample',]
    
    def create(self, validated_data):
        """create override to support writable nested object handling"""
        violations_data = validated_data.pop('violations')
        restaurant_data = validated_data.pop('restaurant')
        # If new restaurant, create it
        r = helpers.get_if_exists(
            Restaurant, restaurant_id=restaurant_data['restaurant_id'])
        if r is None:
            r = Restaurant(**restaurant_data)
            r.save()
        inspection = Inspection.objects.create(
            restaurant_id=r.restaurant_id, **validated_data)
        # update restaurant state, in case of violation failure
        r.is_current = False
        r.save()

        for obj in violations_data:
            violation = Violation.objects.create(
                inspection_id=inspection.inspection_id, **obj)
            InspectionViolation.objects.create(
                inspection_id=inspection.inspection_id, violation=violation)

        r.update_aggregates(num_violations=len(
            violations_data), score=inspection.score)

        return inspection

class OpenFDASerializer(serializers.ModelSerializer):
    drug = DrugSerializer() 

    class Meta:
        model = OpenFDA
        fields = ['manufacturer_name','rxcui','unii','spl_set_id',]

class ActiveIngredientsSerializer(serializers.ModelSerializer):
    drug = DrugSerializer() 

    class Meta:
        model = ActiveIngredients
        fields = ['drug','name','strength']
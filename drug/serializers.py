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
    packaging = PackagingSerializer()
    active_ingredients = ActiveIngredientsSerializer()

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



# A field class that validates a list of objects.

# Signature: ListField(child=<A_FIELD_INSTANCE>, allow_empty=True, min_length=None, max_length=None)

# child - A field instance that should be used for validating the objects in the list. If this argument is not provided then objects in the list will not be validated.
# allow_empty - Designates if empty lists are allowed.
# min_length - Validates that the list contains no fewer than this number of elements.
# max_length - Validates that the list contains no more than this number of elements.
# For example, to validate a list of integers you might use something like the following:

# scores = serializers.ListField(
#    child=serializers.IntegerField(min_value=0, max_value=100)
# )
# The ListField class also supports a declarative style that allows you to write reusable list field classes.

# class StringListField(serializers.ListField):
#     child = serializers.CharField()
# We can now reuse our custom StringListField class throughout our application, without having to provide a child argument to it.
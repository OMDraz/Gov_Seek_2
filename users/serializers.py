from .models import CustomUser
from rest_framework import serializers 
from django_countries.serializer_fields import CountryField

class UserSerializer(serializers.ModelSerializer):
    country = CountryField()
    
    class Meta:
        model = CustomUser 
        fields = ('id','email','STATUS','date_joined','country','age','gender','number_of_prescriptions','weight',)
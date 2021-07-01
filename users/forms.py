from django.contrib.auth.forms import UserCreationForm, UserChangeForm 
from .models import CustomUser 


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('email','country','age','gender','number_of_prescriptions','weight',)

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser 
        fields = ('email','country','age','gender','number_of_prescriptions','weight',)

from django.db import models
from django.utils import timezone 
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django_countries.fields import CountryField
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager



class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        verbose_name='Email address',
        max_length=255,
        unique=True,
    )
    STATUS = (
        (1,  'male'),
        (0,  'female'),
    )
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False) # a admin user; non super-user
    admin = models.BooleanField(default=False) # a superuser
    date_joined = models.DateTimeField(default=timezone.now)
    country = CountryField()
    age = models.IntegerField(blank=True, null=True)
    gender = models.IntegerField(choices=STATUS, default=1)
    number_of_prescriptions = models.IntegerField(default=0)
    weight = models.IntegerField(default=160) 

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [] 

    objects = CustomUserManager() 

    def __str__(self):
        return self.email 
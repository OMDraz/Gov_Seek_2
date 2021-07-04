from django.db import models


class Drug(models.Model):
    product_ndc = models.CharField(max_length=100)
    generic_name = models.CharField(max_length=100)
    labeler_name = models.CharField(max_length=100)
    brand_name = models.CharField(max_length=100)
    active_ingredients = models.ForeignKey('drug.ActiveIngredients', on_delete=models.CASCADE, default='', related_name='+')
    finished = models.BooleanField()
    packaging = models.ForeignKey('drug.Packaging', on_delete=models.CASCADE, default='', related_name='+')
    listing_expiration_date = models.DateField()
    openfda = models.ForeignKey('drug.OpenFDA', on_delete=models.CASCADE, default='', related_name='+')

class ActiveIngredients(models.Model):
    drug = models.ForeignKey(Drug, on_delete=models.CASCADE, default='', related_name='+')    
    name = models.CharField(max_length=100)
    strength = models.CharField(max_length=100)

class Packaging(models.Model):
    drug = models.ForeignKey(Drug, on_delete=models.CASCADE, default='', related_name='+')   
    package_ndc = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    marketing_start_date = models.DateField()
    sample = models.BooleanField()

class OpenFDA(models.Model):
    drug = models.ForeignKey(Drug, on_delete=models.CASCADE, default='', related_name='+')
    manufacturer_name = models.CharField(max_length=100)
    rxcui = models.CharField(max_length=100)
    unii = models.CharField(max_length=100)
    spl_set_id = models.CharField(max_length=100)

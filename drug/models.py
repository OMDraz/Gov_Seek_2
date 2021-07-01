from django.db import models


class Drug(models.Model):
    product_ndc = models.CharField(max_length=100)
    generic_name = models.CharField(max_length=100)
    labeler_name = models.CharField(max_length=100)
    brand_name = models.CharField(max_length=100)
    finished = models.BooleanField()
    listing_expiration_date = models.DateField()
    marketing_category = models.CharField(max_length=100)
    dosage_form = models.CharField(max_length=100)
    spl_id = models.CharField(max_length=100)
    product_type = models.CharField(max_length=100)
    marketing_start_date = models.DateField()
    product_id = models.CharField(max_length=100)
    application_number = models.CharField(max_length=100)
    brand_name_base = models.CharField(max_length=100)

class ActiveIngredients(models.Model):
    drug = models.ForeignKey(Drug, on_delete=models.CASCADE, default=None)    
    name = models.CharField(max_length=100)
    strength = models.CharField(max_length=100)

class Packaging(models.Model):
    drug = models.ForeignKey(Drug, on_delete=models.CASCADE, default=None)   
    package_ndc = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    marketing_start_date = models.DateField()
    sample = models.BooleanField()

class OpenFDA(models.Model):
    drug = models.ForeignKey(Drug, on_delete=models.CASCADE, default=None)
    manufacturer_name = models.TextField(max_length=100)
    rxcui = models.TextField(max_length=100)
    unii = models.TextField(max_length=100)
    spl_set_id = models.TextField(max_length=100)

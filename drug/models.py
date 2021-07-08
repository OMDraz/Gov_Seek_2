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
    marketing_category = models.CharField(max_length=100)
    dosage_form = models.CharField(max_length=100)
    spl_id = models.CharField(max_length=100)
    product_type = models.CharField(max_length=100)
    route = models.CharField(max_length=100)
    marketing_start_date = models.DateField()
    product_id = models.CharField(max_length=100)
    application_number = models.CharField(max_length=100)
    brand_name_base = models.CharField(max_length=100)
    pharm_class = models.CharField(max_length=100)

class ActiveIngredients(models.Model):
    drug = models.ForeignKey(
        Drug,
        to_field='active_ingredients',
        on_delete=models.CASCADE,
        related_name='+'
    )
    name = models.CharField(max_length=100)
    strength = models.CharField(max_length=100)

class Packaging(models.Model):
    drug = models.ForeignKey(
        Drug,
        to_field='packaging',
        on_delete=models.CASCADE,
        related_name='+'
    )
    package_ndc = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    marketing_start_date = models.DateField()
    sample = models.BooleanField()

class OpenFDA(models.Model):
    drug = models.ForeignKey(
        Drug,
        to_field='openfda',
        on_delete=models.CASCADE,
        related_name='+'
    )
    manufacturer_name = models.CharField(max_length=100)
    rxcui = models.CharField(max_length=100)
    unii = models.CharField(max_length=100)
    spl_set_id = models.CharField(max_length=100)

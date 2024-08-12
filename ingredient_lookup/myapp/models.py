from django.db import models

# Create your models here.
class Item(models.Model):
    ingredientName = models.CharField(max_length=200)
    pcode = models.IntegerField()
    casNumber = models.CharField(max_length=50)
    epaRegNumber = models.CharField(max_length=50)
    productName = models.CharField(max_length=200)
    productNameStatus = models.BooleanField()
    redistrationStatus = models.BooleanField()
    productStatusDate = models.DateField()
    alternateBrandName = models.CharField(max_length=200)

    def __str__(self):
        return self.productName

from django.db import models

MAX_NUM_LENGTH = 50
MAX_NAME_LENGTH = 200  
# Create your models here.
class Item(models.Model):
    ingredientName = models.CharField(max_length=MAX_NAME_LENGTH)
    pcode = models.IntegerField()
    casNumber = models.CharField(max_length=MAX_NUM_LENGTH)
    epaRegNumber = models.CharField(max_length=MAX_NUM_LENGTH)
    productName = models.CharField(max_length=MAX_NAME_LENGTH)
    productNameStatus = models.BooleanField()
    registrationStatus = models.BooleanField()
    productStatusDate = models.DateField()
    alternateBrandName = models.CharField(max_length=MAX_NAME_LENGTH)

    def __str__(self):
        return f"{self.productName}"

from enum import unique
from django.db import models
from datetime import * 

# Create your models here.


class ProductGroup(models.Model):
    type = models.CharField(max_length=15)

    def __str__(self) :
        return self.type



class Product(models.Model):
    productgroup = models.ForeignKey(ProductGroup,on_delete=models.CASCADE)
    variety = models.CharField(max_length=15)
    quantity = models.IntegerField()
    price = models.IntegerField()
    star_value = models.DecimalField(max_digits=2, decimal_places=1)
    paking_date = models.DateField()
    expiry_date = models.DateField()
    created_date = models.DateField(default = date.today)
    modified_date = models.DateField(auto_now_add=date.today)

    class Meta:
        unique_together = ("price","quantity")


    def __str__(self) :
        return self.variety

    






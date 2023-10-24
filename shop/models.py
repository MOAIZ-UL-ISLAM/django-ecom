from django.db import models

# Create your models here.

class Product(models.Model):
    title= models.CharField(max_length=200)
    price = models.FloatField()
    discount_price = models.FloatField()
    catagory = models.CharField(max_length=24)
    description = models.TextField()
    image = models.CharField(max_length=500)

    def __str__(self):
        return self.title





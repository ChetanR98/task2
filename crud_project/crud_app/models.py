from django.db import models

# Create your models here.
class Order(models.Model):
    oid = models.IntegerField()
    name = models.CharField(max_length=20)
    mob = models.IntegerField()
    email = models.EmailField()
    add = models.CharField(max_length=100)
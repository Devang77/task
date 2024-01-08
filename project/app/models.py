from django.db import models

# Create your models here.
class user(models.Model):
    username = models.CharField(max_length=100,unique=True)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField(max_length=100,unique=True)
    password = models.CharField(max_length=100,unique=True)
    mobile_number = models.CharField(max_length=100,unique=True)

class customer_detail(models.Model):
    customer_name = models.CharField(max_length=100,unique=True)
    customer_number = models.CharField(max_length=100,unique=True)
    customer_address = models.CharField(max_length=100,unique=True)
    

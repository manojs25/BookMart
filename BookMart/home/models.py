from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=20,null=True)
    mobile = models.IntegerField(primary_key=True)
    email = models.EmailField()
    dob = models.DateField()
    address = models.TextField()
    passwd = models.CharField(max_length=8)

class Order(models.Model):
    uname = models.CharField(max_length=50)
    mobile = models.IntegerField()
    book_name = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    price = models.IntegerField()

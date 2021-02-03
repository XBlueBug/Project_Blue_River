from django.db import models
# from phonenumber_field.modelfields import PhoneNumberField
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class Contact(models.Model):
    name    = models.CharField(max_length=25)
    email   = models.EmailField(max_length=100)
    contact = PhoneNumberField()
    address = models.CharField(max_length=200)
    comment = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    

class User_Registration(models.Model):
    first_name      = models.CharField(max_length=20)
    last_name  = models.CharField(max_length=20)
    email      = models.EmailField(max_length=100)
    address    = models.CharField(max_length=200)
    contact    = PhoneNumberField()
    password   = models.CharField(max_length=14)
    re_enter_password = models.CharField(max_length=14)

    def __str__(self):
        return self.first_name


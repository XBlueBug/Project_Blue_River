from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator, MaxLengthValidator
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

# AREA_CHOICES = ('Bin Qasim Town', 'Baldia Town', 'Clifton Cantonment', 'Faisal Cantonment', 'Gulberg Town',
#  'Gadap Town', 'Gulshan Town', 'Jamshed Town', 'Kemari Town', 'Korangi Town', 'Korangi Industrial Area', 'Korangi Creek Cantonment', 'Lyari Town', 
#  'Landhi Town', 'Malir Town', 'North Nazimabad Town', 'Nazimabad', 'New Karachi Town', 'Orangi Town', 'SITE Town', 
# 'Shah Faisal Town', 'Sur Jani Town')


class Contact(models.Model):
    name    = models.CharField(max_length=25)
    email   = models.EmailField(max_length=100)
    contact = PhoneNumberField()
    address = models.CharField(max_length=200)
    comment = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    

# class Customer(models.Model):
#     user     = models.ForeignKey(User, on_delete=models.CASCADE)
#     name     = models.CharField(max_length=100)
#     address  = models.CharField(max_length=250)
#     # area     = models.CharField(choices=AREA_CHOICES, max_length=50)
#     city     = models.CharField(max_length=50)

#     def __str__(self):
#         return str(self.id)
    


# CATEGORY_CHOICES(
#     ('BW', '19-Liter-Bottel'),
# )

# class Customer_data(models.Model):
#     User = models.ForeignKey(User, on_delete=modles.CASCADE)
#     delivery_date
#     deliverd_bottles
#     empty_bottles
#     bottle_price
#     billed_amount
#     balance_amount
#     payment_status00
#     .03
#     0

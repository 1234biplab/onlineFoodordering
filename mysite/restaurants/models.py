from django.db import models
from address.models import Address
# Create your models here.
from datetime import date

class RestaurantAccount(models.Model):
    username = models.CharField(max_length=20, verbose_name='Username',unique=True)
    email = models.EmailField(max_length=60, verbose_name='Enter Email')
    password = models.CharField(max_length=50, verbose_name='Enter Password')
    mobile = models.CharField(max_length=20, verbose_name='Enter Mobile')


    def __str__(self):
        return self.username + " - " + self.email

class Restaurant(models.Model):
    image = models.ImageField(upload_to="restaurants", blank=True, null=True, default='default.png')
    name = models.CharField(max_length=200)
    street = models.CharField(max_length=200, blank=True, null=True)
    mobile = models.CharField(max_length=200, blank=True, null=True)
    zipCode = models.CharField(max_length=200, blank=True, null=True)

    website_url = models.URLField(blank=True, null=True)
    restaurant_user = models.ForeignKey(RestaurantAccount,on_delete=models.CASCADE)
    date = models.DateField(default=date.today)

    address = models.ForeignKey(Address, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
from django.db import models

# Create your models here.
class Country(models.Model):
    country = models.CharField(max_length=20)
    def __str__(self):
        return self.country


class State(models.Model):
    state = models.CharField(max_length=20)
    country = models.ForeignKey(Country,on_delete=models.CASCADE)

    def __str__(self):
        return self.state


class City(models.Model):
    city = models.CharField(max_length=20)
    state = models.ForeignKey(State,on_delete=models.CASCADE)

    def __str__(self):
        return self.city


class Address(models.Model):

    street =models.CharField(max_length=20)
    gali = models.CharField(max_length=10)
    postal = models.CharField(max_length=6)
    country = models.ForeignKey(Country,on_delete=models.CASCADE)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)

    def __str__(self):
        return self.postal
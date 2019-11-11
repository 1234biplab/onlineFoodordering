from django.db import models
from datetime import date
from restaurants.models import Restaurant


class Cotergory(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural ='categories'


    def __str__(self):
        return self.name



class Menu(models.Model):
    category = models.ForeignKey(Cotergory, on_delete=models.CASCADE)

    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField('Price Rs.', max_digits=8, decimal_places=2, blank=True, null=True)
    offer_price = models.DecimalField('Offrer Rs.', max_digits=8, decimal_places=2, blank=True, null=True)
    date = models.DateField(default=date.today)
    image = models.ImageField(upload_to="food", blank=True, null=True, default='default.png')
    restaurant = models.ForeignKey(Restaurant, null=True, on_delete=models.CASCADE)
    stock = models.PositiveIntegerField()
    available = models.BooleanField(default=True)
    updated = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name


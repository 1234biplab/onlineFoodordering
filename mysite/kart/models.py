from django.db import models

# Create your models here.
class Kart(models.Model):
    menu = models.CharField(max_length=255, default="1" )
    slug = models.SlugField(max_length=200, db_index=True, default="1")


class KartFood(models.Model):
    dish_name = models.CharField(max_length=200)
    dish_price = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    dish_qty = models.IntegerField(null=True)

    def __str__(self):
        return self.dish_name
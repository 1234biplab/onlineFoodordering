from django.contrib import admin

# Register your models here.
from .models import RestaurantAccount,Restaurant
# Register your models here.

admin.site.register(RestaurantAccount)
admin.site.register(Restaurant)
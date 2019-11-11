from django.contrib import admin

# Register your models here.
from .models import City,Country,State,Address
# Register your models here.

admin.site.register(Country)
admin.site.register(State)
admin.site.register(City)
admin.site.register(Address)
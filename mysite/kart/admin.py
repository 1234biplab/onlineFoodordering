from django.contrib import admin

# Register your models here.
from .models import Kart,KartFood

admin.site.register(Kart)
admin.site.register(KartFood)
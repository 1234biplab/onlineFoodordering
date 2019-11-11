from django.contrib import admin
from .models import Menu,Cotergory
# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name','slug']
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Cotergory,CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','slug','category','stock','price','available']
    list_filter = ['available','date','updated','category']
    list_editable = ['price','stock','available']
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Menu,ProductAdmin)

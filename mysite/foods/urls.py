
from django.urls import path,include
from django.contrib import admin

from . import views as food_views

urlpatterns = [
    path('', food_views.all_foods,name='home'),
    path('foods/', food_views.all_foods_only,name='foods_all'),
    path('details/<int:id>', food_views.food_details,name='details'),
    path('show_detail/<int:id>', food_views.res_details,name='show_res'),
    path('kart/<int:id>',include('kart.urls'),name='cart'),


]

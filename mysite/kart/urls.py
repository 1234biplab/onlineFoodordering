
from django.urls import path,include


from . import views as kart_views


urlpatterns = [
   path('', kart_views.food_cart,name='cart'),
   path('withlist/', kart_views.withlist,name='withlist_kart'),
   path('delete/<int:id>', kart_views.delete_food,name='delete_food'),
   path('checkout/', kart_views.checkout,name='food_checkout'),
   path('payment/', kart_views.payment,name='payment'),




]

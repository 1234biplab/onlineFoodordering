
from django.urls import path

from . import views as up_views

urlpatterns = [
    path('',up_views.user_proile,name='userprofile'),
    path('update/<int:id>',up_views.update_profile, name='update_profile'),
]

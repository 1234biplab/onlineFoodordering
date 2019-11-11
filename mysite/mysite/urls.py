
from django.urls import path,include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),

    path('',include('foods.urls'),name='foods'),
    path('accounts/',include('Accounts.urls'),name='account'),
    # url(r'^',include('foods.urls')),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.contrib import admin
from django.urls import path, include
from marketplace import views as marketplace_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('marketplace/', include('marketplace.urls')),
    path('', marketplace_views.home, name='home'),  # Handle root URL
]

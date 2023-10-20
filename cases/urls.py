from django.urls import path, include

from .views import homepage_shower


urlpatterns = [
    path('', homepage_shower, name='home'),
]


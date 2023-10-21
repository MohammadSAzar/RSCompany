from django.urls import path, include

from .views import home_shower


urlpatterns = [
    path('', home_shower, name='home'),
]


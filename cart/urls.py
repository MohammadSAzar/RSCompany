from django.urls import path
from .views import cart_detail_view, add_to_cart_view


urlpatterns = [
    path('add/<int:case_id>/', add_to_cart_view, name='cart_add'),
    path('', cart_detail_view, name='cart_detail'),
]


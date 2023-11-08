from django.db import models
from django.utils.translation import gettext as _
from django.conf import settings

from cases.models import Case


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name=_('User'))
    first_name = models.CharField(max_length=150, verbose_name=_('First Name'))
    last_name = models.CharField(max_length=150, verbose_name=_('Last Name'))
    phone = models.CharField(max_length=11, verbose_name=_('Phone Number'))
    national_code = models.CharField(max_length=10, verbose_name=_('national_code'))
    address = models.CharField(max_length=1000, verbose_name=_('Address'))
    is_paid = models.BooleanField(default=False, verbose_name=_('Is_Paid?'))
    notes = models.CharField(max_length=1000, verbose_name=_('Notes'))
    datetime_created = models.DateTimeField(auto_now_add=True, verbose_name=_('date & time of creation'))
    datetime_modified = models.DateTimeField(auto_now=True, verbose_name=_('date & time of modification'))

    def get_total_price(self):
        return sum(item.meter*item.price for item in self.item.all())

    def __str__(self):
        return f'Order: {self.id}'

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='item')
    case = models.ForeignKey(Case, on_delete=models.CASCADE, related_name='order_items')
    meter = models.PositiveIntegerField(default=1)
    base_value = models.PositiveIntegerField()

    def __str__(self):
        return f'Order Item {self.id}: {self.case}x{self.meter}'




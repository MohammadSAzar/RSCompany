from django.contrib import admin
from jalali_date.admin import ModelAdminJalaliMixin

from .models import Order, OrderItem

class ItemsInOrdersInline(admin.TabularInline):
    model = OrderItem
    fields = ('order', 'case', 'meter', 'price',)
    extra = 1

@admin.register(Order)
class OrderAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    list_display = ('user', 'first_name', 'last_name', 'is_paid', 'national_code', 'datetime_created',)
    ordering = ('-datetime_created', )
    inlines = [
        ItemsInOrdersInline,
    ]

@admin.register(OrderItem)
class OrderItemAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    list_display = ('order', 'case', 'meter', 'price',)



from django.contrib import admin

from .models import Case


@admin.register(Case)
class CaseAdmin(admin.ModelAdmin):
    list_display = ('title', 'maker', 'city', 'region', 'capacity', 'base_value', 'buy_assurance',
                    'guaranteed_gain', 'guaranteed_gain_percent', 'end_time', 'status', 'datetime_created')
    ordering = ('-datetime_created', )
    prepopulated_fields = {'slug': ('title',)}
    # inlines = [
    #     ReviewInProductInline,
    # ]

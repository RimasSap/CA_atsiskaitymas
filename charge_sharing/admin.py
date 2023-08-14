from django.contrib import admin
from .models import ElectricityPrice

# Register your models here.


class ElectricityPriceAdmin(admin.ModelAdmin):
    list_display = ('year', 'month', 'day', 'hour', 'electricity_price')
    list_filter = ('year', 'month', 'day', 'hour')
    search_fields = ('year', 'month', 'day', 'hour')


admin.site.register(ElectricityPrice, ElectricityPriceAdmin)


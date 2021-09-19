from django.contrib import admin
from .models import Address, Country, State


# ================================================================== >> Country
@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    search_fields = ['name', 'shortcut']
    list_display = ('name', 'shortcut')
    list_editable = ('shortcut',)


# =============================================================================
# State
@admin.register(State)
class StateAdmin(admin.ModelAdmin):
    search_fields = ['name', 'country__name']
    autocomplete_fields = ['country']
    list_editable = ('name', 'shortcut',)
    list_display = ('country', 'name', 'shortcut')


# ================================================================== >> Address
@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    search_fields = ['street', 'city', 'state__name', 'zipcode']
    autocomplete_fields = ['state']
    list_display = ('street', 'hn', 'zipcode', 'city', 'state')

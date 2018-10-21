from django.contrib import admin

from housing.models import House


class HouseAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'price',)


admin.site.register(House, HouseAdmin)

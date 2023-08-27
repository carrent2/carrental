from django.contrib import admin
from .models import Rental, UserProfile, Car
from django.utils.html import format_html

admin.site.register(UserProfile)

@admin.register(Rental)
class RentalAdmin(admin.ModelAdmin):
    list_display = ('car', 'user', 'start_date', 'end_date', 'price')
    search_fields = ('car', 'user')

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('brand', 'model', 'year', 'display_image')

    def display_image(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="90" height="50" />', obj.image.url)
        else:
            return format_html('<span>No Image</span>')

    display_image.short_description = 'Image'




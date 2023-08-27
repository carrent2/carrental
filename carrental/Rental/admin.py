from django.contrib import admin
from .models import Rental, UserProfile, Car

#admin.site.register(Rental)
admin.site.register(UserProfile)
admin.site.register(Car)


@admin.register(Rental)
class RentalAdmin(admin.ModelAdmin):
    list_display = ('car', 'user', 'start_date', 'end_date', 'price')
    search_fields = ('car', 'user')
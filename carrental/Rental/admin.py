from django.contrib import admin

from .models import Rental, UserProfile, Car


admin.site.register(Rental)

admin.site.register(UserProfile)

admin.site.register(Car)

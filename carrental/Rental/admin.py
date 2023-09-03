from django.contrib import admin
from .models import Rental, UserProfile, Car, Comment, ContactMessage
from django.utils.html import format_html


admin.site.register(UserProfile)

@admin.register(Rental)
class RentalAdmin(admin.ModelAdmin):
    list_display = ('id', 'car', 'user', 'start_date', 'end_date','created_at','updated_at', 'price')
    search_fields = ('car', 'user')

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('brand', 'model', 'year', 'description', 'display_image')

    def display_image(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="90" height="50" />', obj.image.url)
        else:
            return format_html('<span>No Image</span>')

    display_image.short_description = 'Image'

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user','car', 'created', 'updated')
    list_filter = ('active', 'created', 'updated')
    search_fields = ('user', 'email', 'body')

@admin.register(ContactMessage)
class ContactMessage_admin(admin.ModelAdmin):
    list_display = ('email','message')
    search_fields = ('email', 'message')






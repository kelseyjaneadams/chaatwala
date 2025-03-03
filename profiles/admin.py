from django.contrib import admin
from .models import Profile

# Register your models here.


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """
    Admin interface for managing user profiles.
    Displays user and profile image in the admin panel.
    """
    list_display = ('user', 'image')
    search_fields = ('user__username',)

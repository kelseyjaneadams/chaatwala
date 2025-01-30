from django.contrib import admin
from .models import Review
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
@admin.register(Review)
class ReviewAdmin(SummernoteModelAdmin):
    """
    Admin interface for managing reviews.
    Enables Summernote for the comment field and provides
    additional configurations for list display and filtering,
    """
    summernote_fields = ('comment',)
    list_display = ('user', 'rating', 'created_on')
    list_filter = ('rating', 'created_on')
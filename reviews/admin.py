from django.contrib import admin
from .models import Review
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
@admin.register(Review)
class ReviewAdmin(SummernoteModelAdmin):
    """
    Admin interface for managing reviews.
    Enables Summernote for the comment field and provides
    additional configurations for list display, filtering, and search.
    """
    summernote_fields = ('comment',)
    list_display = ('review_id', 'user', 'rating', 'review_date')
    list_filter = ('rating', 'review_date')
    search_fields = ('review_id', 'user__username')

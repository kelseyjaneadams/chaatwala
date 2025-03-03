from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Review


@admin.register(Review)
class ReviewAdmin(SummernoteModelAdmin):
    """
    Admin interface for managing reviews.

    - Enables Summernote for the comment field.
    - Displays relevant review details in the list view.
    - Allows filtering by review status, rating, and creation date.
    - Orders "pending" reviews first, followed by the newest reviews.
    """

    summernote_fields = ("comment",)
    list_display = ("user", "rating", "status", "created_on")
    list_filter = ("status", "rating", "created_on")
    ordering = ["status", "-created_on"]

    def get_ordering(self, request):
        """
        Ensures 'pending' reviews appear first in the list,
        followed by the most recently created reviews.
        """
        return ["status", "-created_on"]

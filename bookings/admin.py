from django.contrib import admin
from .models import Booking
from django_summernote.admin import SummernoteModelAdmin
from .forms import CustomTimeForm


# Register your models here.
@admin.register(Booking)
class BookingAdmin(SummernoteModelAdmin):
    """
    Admin customisation for the Booking model.

    - Integrates Summernote for the 'special_request' field.
    - Customises the list view to display booking details.
    - Adds filters for status and booking date.
    - Enables search functionality for booking ID and user.
    - Uses a custom form to add dropdowns for booking_time.
    """
    summernote_fields = ('special_request',)
    list_display = (
        'booking_id',
        'user',
        'number_of_guests',
        'booking_date',
        'booking_time',
        'status',
    )
    list_filter = ('status', 'booking_date')
    search_fields = ('booking_id', 'user__username')
    form = CustomTimeForm

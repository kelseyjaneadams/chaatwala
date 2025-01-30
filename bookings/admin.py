from django.contrib import admin
from .models import Booking
from django_summernote.admin import SummernoteModelAdmin
from .forms import CustomTimeForm


@admin.register(Booking)
class BookingAdmin(SummernoteModelAdmin):
    """
    Admin customization for the Booking model.

    - Integrates Summernote for the 'special_request' field.
    - Customizes the list view to display booking details.
    - Adds filters for status and booking date.
    - Uses a custom form to provide dropdowns for hour and minute fields.
    """
    summernote_fields = ('special_request',)
    list_display = (
        'user',
        'contact_name',
        'number_of_guests',
        'booking_date',
        'booking_time',
        'status',
    )
    list_filter = ('status', 'booking_date')
    form = CustomTimeForm
from django.db import models
from django.contrib.auth.models import User


class Booking(models.Model):
    """
    Stores a single booking entry related to :model:`auth.User`.
    Each booking includes a unique ID, a contact name (optional),
    the number of guests, booking date and time, an optional special 
    request, and the booking status. The booking is associated with 
    a specific user who created it.
    """
    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('CONFIRMED', 'Confirmed'),
        ('CANCELLED', 'Cancelled'),
    ]

    booking_id = models.CharField(
        primary_key=True,
        max_length=50
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    contact_name = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )
    number_of_guests = models.IntegerField()
    booking_date = models.DateField()
    booking_time = models.TimeField()
    special_request = models.CharField(
        max_length=255,
        blank=True,
        null=True
    )
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='PENDING' 
    )

    def __str__(self):
        return f"Booking {self.booking_id} by {self.user.username}"


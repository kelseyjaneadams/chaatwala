from django.db import models
from django.contrib.auth.models import User


class Booking(models.Model):
    STATUS_PENDING = 'PENDING'
    STATUS_CONFIRMED = 'CONFIRMED'
    STATUS_CANCELLED = 'CANCELLED'

    STATUS_CHOICES = [
        (STATUS_PENDING, 'Pending'),
        (STATUS_CONFIRMED, 'Confirmed'),
        (STATUS_CANCELLED, 'Cancelled'),
    ]

    GUEST_CHOICES = [(i, str(i)) for i in range(1, 7)]

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    contact_name = models.CharField(
        max_length=50,
    )
    number_of_guests = models.IntegerField(
        choices=GUEST_CHOICES
    )
    booking_date = models.DateField()
    booking_time = models.TimeField()
    special_request = models.TextField(
        max_length=500,
        blank=True,
        null=True
    )
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default=STATUS_PENDING
    )

    def __str__(self):
        return (
        f"Booking by {self.user.username} for "
        f"{self.number_of_guests} guests"
    )
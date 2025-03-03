from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils.timezone import now


class Booking(models.Model):
    """Model representing a table booking."""

    STATUS_PENDING = "PENDING"
    STATUS_CONFIRMED = "CONFIRMED"
    STATUS_CANCELLED = "CANCELLED"

    STATUS_CHOICES = [
        (STATUS_PENDING, "Pending"),
        (STATUS_CONFIRMED, "Confirmed"),
        (STATUS_CANCELLED, "Cancelled"),
    ]

    GUEST_CHOICES = [(i, str(i)) for i in range(1, 7)]

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    contact_name = models.CharField(
        max_length=50,
        blank=False
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

    def clean(self):
        """Validate that booking date is not in the past."""
        if self.booking_date and self.booking_date < now().date():
            raise ValidationError("You cannot book a date in the past.")

    def save(self, *args, **kwargs):
        """Reset status to 'PENDING' if a confirmed booking is updated."""
        if self.pk:
            original = Booking.objects.get(pk=self.pk)
            if (
                original.status == self.STATUS_CONFIRMED
                and (
                    original.booking_date != self.booking_date
                    or original.booking_time != self.booking_time
                    or original.number_of_guests != self.number_of_guests
                )
            ):
                self.status = self.STATUS_PENDING

        self.clean()
        super().save(*args, **kwargs)

    def __str__(self):
        """String representation of the booking."""
        return (
            f"Booking by {self.user.username} for {self.number_of_guests} "
            f"guests on {self.booking_date} at {self.booking_time}"
        )

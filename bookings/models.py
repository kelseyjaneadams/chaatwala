from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_save
from django.dispatch import receiver


class Booking(models.Model):
    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('CONFIRMED', 'Confirmed'),
        ('CANCELLED', 'Cancelled'),
    ]

    booking_id = models.CharField(
        primary_key=True,
        max_length=50,
        editable=False,
        unique=True
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    contact_name = models.CharField(max_length=100, blank=True, null=True)
    number_of_guests = models.IntegerField()
    booking_date = models.DateField()
    booking_time = models.TimeField()
    special_request = models.TextField(blank=True, null=True)
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='PENDING'
    )

    def __str__(self):
        return f"Booking {self.booking_id} by {self.user.username}"


@receiver(pre_save, sender=Booking)
def set_booking_id(sender, instance, **kwargs):
    if not instance.booking_id:
        last_booking = Booking.objects.order_by('booking_id').last()
        next_id = int(last_booking.booking_id.replace("BOOK", "")) + 1 if last_booking else 1
        instance.booking_id = f"BOOK{next_id:03d}"

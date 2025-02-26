from django.test import TestCase
from django.contrib.auth.models import User
from bookings.models import Booking
from datetime import date, time
from django.core.exceptions import ValidationError


class BookingModelTest(TestCase):
    """Test case for the Booking model."""

    def setUp(self):
        """Set up a user and a booking instance before each test."""
        self.user = User.objects.create_user(
            username="testuser",
            password="password123"
        )

        self.booking = Booking.objects.create(
            user=self.user,
            contact_name="John Doe",
            number_of_guests=2,
            booking_date=date(2025, 3, 15),
            booking_time=time(18, 30),
            special_request="Near the window",
            status=Booking.STATUS_PENDING
        )

    def test_booking_str_representation(self):
        """Test the __str__ method of the Booking model."""
        expected_str = (
            "Booking by testuser for 2 guests "
            "on 2025-03-15 at 18:30:00"
        )
        self.assertEqual(str(self.booking), expected_str)

    def test_default_status_is_pending(self):
        """Test that the default status of a booking is 'PENDING'."""
        new_booking = Booking.objects.create(
            user=self.user,
            contact_name="Jane Doe",
            number_of_guests=3,
            booking_date=date(2025, 4, 20),
            booking_time=time(19, 0)
        )
        self.assertEqual(new_booking.status, Booking.STATUS_PENDING)

    def test_number_of_guests_choices(self):
        """Test that number_of_guests must be one of the defined choices."""
        invalid_booking = Booking(
            user=self.user,
            contact_name="Invalid Test",
            number_of_guests=10,
            booking_date=date(2025, 5, 10),
            booking_time=time(20, 0)
        )

        with self.assertRaises(ValidationError) as context:
            invalid_booking.full_clean()

        self.assertIn("number_of_guests", context.exception.message_dict)

    def test_booking_creation(self):
        """Test that a booking instance is created properly."""
        self.assertEqual(Booking.objects.count(), 1)

    def test_booking_deletion_when_user_deleted(self):
        """Test that deleting a user also deletes their bookings."""
        self.user.delete()
        self.assertEqual(Booking.objects.count(), 0)

    def test_booking_date_cannot_be_in_the_past(self):
        """Test that booking a past date raises a validation error."""
        past_booking = Booking(
            user=self.user,
            contact_name="Past Booking",
            number_of_guests=2,
            booking_date=date(2023, 1, 1),
            booking_time=time(18, 0)
        )

        with self.assertRaises(ValidationError) as context:
            past_booking.full_clean()

        self.assertIn("You cannot book a date in the past.", str(context.exception))
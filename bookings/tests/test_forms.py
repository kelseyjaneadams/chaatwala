from django.test import TestCase
from django.contrib.auth.models import User
from bookings.forms import BookingForm
from datetime import date


class BookingFormTest(TestCase):
    """Test case for the BookingForm."""

    def setUp(self):
        """Set up a test user before each test."""
        self.user = User.objects.create_user(
            username="testuser",
            password="password123"
        )

    def test_valid_booking_form(self):
        """Test form with valid data."""
        form_data = {
            "contact_name": "John Doe",
            "number_of_guests": 2,
            "booking_date": date.today(),
            "hour": "6",
            "minute": "30",
            "special_request": "Near window"
        }
        form = BookingForm(data=form_data)
        self.assertTrue(form.is_valid(), form.errors)

    def test_missing_required_fields(self):
        """Test form fails validation when required fields are missing."""
        form_data = {}
        form = BookingForm(data=form_data)

        self.assertFalse(form.is_valid())
        self.assertIn("contact_name", form.errors)
        self.assertIn("number_of_guests", form.errors)
        self.assertIn("booking_date", form.errors)
        self.assertIn("hour", form.errors)
        self.assertIn("minute", form.errors)

    def test_invalid_hour_choice(self):
        """Test that an invalid hour choice raises a validation error."""
        form_data = {
            "contact_name": "John Doe",
            "number_of_guests": 2,
            "booking_date": date.today(),
            "hour": "11",
            "minute": "30",
        }
        form = BookingForm(data=form_data)

        self.assertFalse(form.is_valid())
        self.assertIn("hour", form.errors)

    def test_clean_method_sets_booking_time(self):
        """Test that the clean() method correctly sets booking_time."""
        form_data = {
            "contact_name": "Jane Doe",
            "number_of_guests": 3,
            "booking_date": date.today(),
            "hour": "5",
            "minute": "15",
            "special_request": "Quiet area"
        }
        form = BookingForm(data=form_data)

        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data["booking_time"], "5:15")

    def test_save_sets_booking_time(self):
        """Test that save() correctly updates the booking_time field."""
        form_data = {
            "contact_name": "Alice Doe",
            "number_of_guests": 4,
            "booking_date": date.today(),
            "hour": "7",
            "minute": "45",
            "special_request": "Balcony"
        }
        form = BookingForm(data=form_data)

        self.assertTrue(form.is_valid())
        booking = form.save(commit=False)
        self.assertEqual(booking.booking_time, "7:45")
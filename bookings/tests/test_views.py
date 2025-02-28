from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from bookings.models import Booking
from reviews.models import Review
from datetime import date, time


class BookingViewsTest(TestCase):
    """Test case for the Booking app views."""

    def setUp(self):
        """Set up a test client, user, and sample bookings."""
        self.client = Client()
        self.user = User.objects.create_user(
            username="testuser", password="password123"
        )
        self.client.login(username="testuser", password="password123")

        self.booking = Booking.objects.create(
            user=self.user,
            contact_name="John Doe",
            number_of_guests=2,
            booking_date=date(2025, 3, 15),
            booking_time=time(18, 30),
            special_request="Near the window",
            status=Booking.STATUS_PENDING
        )

        self.review = Review.objects.create(
            user=self.user,
            comment="Great food!",
            rating=5,
            status="approved",
        )

    def test_my_bookings_view(self):
        """Test that my_bookings loads correctly and displays the booking form."""
        response = self.client.get(reverse("bookings"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "bookings/bookings.html")

        self.assertContains(response, "Book a Table")
        self.assertContains(response, "contact_name")
        self.assertContains(response, "number_of_guests")
        self.assertContains(response, "booking_date")
        self.assertContains(response, "hour")
        self.assertContains(response, "minute")
        self.assertContains(response, "special_request")

    def test_profile_page_displays_bookings(self):
        """Test that the profile page correctly displays the user's bookings."""
        response = self.client.get(reverse("profile"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "profiles/profile.html")

        formatted_date = self.booking.booking_date.strftime("%B %d, %Y")

        self.assertContains(response, "Your Bookings")
        self.assertContains(response, formatted_date)
        self.assertContains(response, str(self.booking.number_of_guests))
        self.assertContains(response, self.booking.get_status_display())

    def test_book_table_valid(self):
        """Test booking submission with valid data."""
        form_data = {
            "contact_name": "Alice",
            "number_of_guests": 3,
            "booking_date": "2025-04-10",
            "hour": "5",
            "minute": "30",
            "special_request": "Birthday celebration",
        }
        response = self.client.post(reverse("book_table"), data=form_data, follow=True)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Thanks for booking with us! Your booking is pending approval.")
        self.assertEqual(Booking.objects.count(), 2)

    def test_book_table_invalid(self):
        """Test booking submission with missing required fields."""
        form_data = {}
        response = self.client.post(reverse("book_table"), data=form_data)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "There was an error with your booking.")

    def test_edit_booking_view(self):
        """Test that an existing booking can be edited successfully."""
        edit_url = reverse("edit_booking", args=[self.booking.id])
        form_data = {
            "contact_name": "Updated Name",
            "number_of_guests": 4,
            "booking_date": "2025-05-15",
            "hour": "6",
            "minute": "45",
            "special_request": "Updated request",
        }
        response = self.client.post(edit_url, data=form_data, follow=True)

        self.booking.refresh_from_db()
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Your booking has been updated")
        self.assertEqual(self.booking.contact_name, "Updated Name")

    def test_delete_booking_view(self):
        """Test that a booking is deleted successfully."""
        delete_url = reverse("delete_booking", args=[self.booking.id])
        response = self.client.post(delete_url, follow=True)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Your booking has been deleted.")
        self.assertFalse(Booking.objects.filter(id=self.booking.id).exists())

    def test_unauthenticated_access_redirects(self):
        """Ensure unauthenticated users are redirected from protected views."""
        self.client.logout()

        protected_urls = [
            reverse("bookings"),
            reverse("book_table"),
            reverse("edit_booking", args=[self.booking.id]),
            reverse("delete_booking", args=[self.booking.id]),
            reverse("profile"),
        ]

        for url in protected_urls:
            response = self.client.get(url, follow=True)
            self.assertRedirects(response, f"/accounts/login/?next={url}")
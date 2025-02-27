from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.timezone import now
from django.core.files.uploadedfile import SimpleUploadedFile
from profiles.models import Profile
from bookings.models import Booking
from reviews.models import Review
from datetime import time


class ProfileViewsTest(TestCase):
    """Test case for the Profile app views."""

    def setUp(self):
        """Set up a test client, user, profile, and sample data."""
        self.client = Client()
        self.user = User.objects.create_user(
            username="testuser", password="password123"
        )
        self.client.login(username="testuser", password="password123")

        self.profile = Profile.objects.get(user=self.user)

        self.booking = Booking.objects.create(
            user=self.user,
            contact_name="John Doe",
            number_of_guests=2,
            booking_date=now().date(),
            booking_time=time(18, 30),
            special_request="Near the window",
            status=Booking.STATUS_PENDING
        )

        self.review = Review.objects.create(
            user=self.user,
            rating=5,
            comment="Great food!",
            status="approved"
        )

    def test_profile_page_loads(self):
        """Test that the profile page loads successfully for logged-in users."""
        response = self.client.get(reverse("profile"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "profiles/profile.html")

    def test_profile_page_displays_bookings_and_reviews(self):
        """Test that the profile page displays the user's bookings and reviews."""
        response = self.client.get(reverse("profile"))

        formatted_date = self.booking.booking_date.strftime("%B %d, %Y")

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Your Bookings")
        self.assertContains(response, formatted_date)
        self.assertContains(response, str(self.booking.number_of_guests))
        self.assertContains(response, self.booking.get_status_display())

        self.assertContains(response, "Your Reviews")
        self.assertContains(response, self.review.comment)

    def test_profile_picture_update_success(self):
        """Test that a user can successfully update their profile picture."""
        image = SimpleUploadedFile(
            name="test_image.jpg",
            content=b"\x47\x49\x46\x38\x39\x61\x01\x00\x01\x00\x00\xff\x00\xff\x00\xff\x00!",
            content_type="image/jpeg"
        )

        response = self.client.post(
            reverse("profile"),
            {"image": image},
            follow=True
        )

        self.assertEqual(response.status_code, 200)
        self.profile.refresh_from_db()
        self.assertTrue(self.profile.image)

    def test_profile_picture_update_no_image(self):
        """Test that submitting an empty form does not update the profile image."""
        response = self.client.post(reverse("profile"), {}, follow=True)
        self.assertEqual(response.status_code, 200)

    def test_unauthenticated_user_redirect(self):
        """Test that unauthenticated users are redirected to login."""
        self.client.logout()
        response = self.client.get(reverse("profile"), follow=True)
        self.assertRedirects(response, "/accounts/login/?next=/profiles/")
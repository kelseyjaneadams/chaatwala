from django.test import SimpleTestCase
from django.urls import resolve, reverse
from profiles.views import profile_view
from django.test import TestCase, Client
from django.contrib.auth.models import User


class TestProfileURLs(SimpleTestCase):
    """Test case for profile app URLs."""

    def test_profile_url_resolves(self):
        """Test that the profile URL correctly resolves to the profile_view."""
        url = reverse("profile")
        self.assertEqual(resolve(url).func, profile_view)


class TestProfileAccess(TestCase):
    """Test case for profile URL access."""

    def setUp(self):
        """Set up a test client and user."""
        self.client = Client()
        self.user = User.objects.create_user(
            username="testuser", password="password123"
        )
        self.profile_url = reverse("profile")

    def test_authenticated_user_can_access_profile(self):
        """Test that an authenticated user can access the profile page."""
        self.client.login(username="testuser", password="password123")
        response = self.client.get(self.profile_url)
        self.assertEqual(response.status_code, 200)

    def test_unauthenticated_user_redirected_to_login(self):
        """Test that an unauthenticated user is redirected to login."""
        response = self.client.get(self.profile_url, follow=True)
        login_url = f"/accounts/login/?next={self.profile_url}"
        self.assertRedirects(response, login_url)

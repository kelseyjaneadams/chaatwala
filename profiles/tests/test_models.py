from django.test import TestCase
from django.contrib.auth.models import User
from profiles.models import Profile


class ProfileModelTest(TestCase):
    """Test case for the Profile model."""

    def setUp(self):
        """Set up a test user and profile instance."""
        self.user = User.objects.create_user(
            username="testuser", password="password123"
        )
        self.profile = Profile.objects.get(user=self.user)

    def test_profile_creation(self):
        """Test that a profile is automatically created for a new user."""
        self.assertEqual(self.profile.user, self.user)
        self.assertEqual(self.profile.image, "profile_pics/default")

    def test_profile_str_representation(self):
        """Test the __str__ method of the Profile model."""
        expected_str = "testuser's Profile"
        self.assertEqual(str(self.profile), expected_str)

    def test_profile_deletion_with_user(self):
        """Test that deleting a user also deletes the associated profile."""
        self.user.delete()
        self.assertFalse(Profile.objects.filter(user=self.user).exists())
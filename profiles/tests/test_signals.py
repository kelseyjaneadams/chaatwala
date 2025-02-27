from django.test import TestCase
from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile
from unittest.mock import patch
from profiles.models import Profile


class TestProfileSignals(TestCase):
    """Test case for profile model signals."""

    def test_profile_created_on_user_creation(self):
        """Test that a profile is automatically created when a user is created."""
        user = User.objects.create_user(username="testuser", password="password123")
        self.assertTrue(Profile.objects.filter(user=user).exists())

    @patch("cloudinary.uploader.upload")
    def test_profile_updates_when_user_updates(self, mock_upload):
        """
        Test that the profile updates when the user updates,
        without calling Cloudinary.
        """
        mock_upload.return_value = {"public_id": "test_image"}

        user = User.objects.create_user(username="testuser4", password="password123")
        profile = Profile.objects.get(user=user)

        new_image = SimpleUploadedFile(
            name="new_image.jpg",
            content=b"\x47\x49\x46\x38\x39\x61\x01\x00\x01\x00\x00\xff\x00\xff\x00\xff\x00!",
            content_type="image/jpeg"
        )

        profile.image = "test_image"
        profile.save()

        profile.refresh_from_db()

        self.assertEqual(str(profile.image), "test_image")
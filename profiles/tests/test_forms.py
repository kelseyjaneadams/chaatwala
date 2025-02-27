from django.test import TestCase
from profiles.forms import ProfileImageForm
from django.core.files.uploadedfile import SimpleUploadedFile
from PIL import Image
import io


class ProfileImageFormTest(TestCase):
    """Test case for the ProfileImageForm."""

    def generate_test_image(self):
        """Generate a valid in-memory image file for testing."""
        image = Image.new("RGB", (100, 100), color="red")
        image_io = io.BytesIO()
        image.save(image_io, format="JPEG")
        image_io.seek(0)
        return SimpleUploadedFile("test_image.jpg", image_io.getvalue(), content_type="image/jpeg")

    def test_valid_form(self):
        """Test that the form is valid with a valid image file."""
        image_file = self.generate_test_image()
        form_data = {"image": image_file}
        form = ProfileImageForm(data={}, files=form_data)

        self.assertTrue(form.is_valid())

    def test_missing_image_field(self):
        """Test that the form is invalid if no image is provided."""
        form = ProfileImageForm(data={})

        self.assertFalse(form.is_valid())
        self.assertIn("image", form.errors)
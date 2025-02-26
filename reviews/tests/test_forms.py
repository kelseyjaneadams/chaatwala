from django.test import TestCase
from reviews.forms import ReviewForm


class ReviewFormTest(TestCase):
    """Test case for the ReviewForm."""

    def test_valid_form(self):
        """Test that the form is valid when all required fields are provided."""
        form_data = {
            "rating": 5,
            "comment": "Excellent service and great food!",
        }
        form = ReviewForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_form_missing_fields(self):
        """Test that the form is invalid if required fields are missing."""
        form_data = {
            "rating": "",
            "comment": "",
        }
        form = ReviewForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn("rating", form.errors)
        self.assertIn("comment", form.errors)

    def test_comment_max_length(self):
        """Test that the comment field enforces a maximum length of 500 characters."""
        long_comment = "A" * 501
        
        form_data = {
            "rating": 3,
            "comment": long_comment,
        }
        form = ReviewForm(data=form_data)

        self.assertFalse(form.is_valid())
        self.assertIn("comment", form.errors)

        self.assertIn("Ensure this value has at most 500 characters", form.errors["comment"][0])


    def test_comment_placeholder(self):
        """Ensure the comment field has the correct placeholder and attributes."""
        form = ReviewForm()
        self.assertEqual(
            form.fields["comment"].widget.attrs["placeholder"],
            "Write your review here..."
        )
        self.assertEqual(
            form.fields["comment"].widget.attrs["aria-label"],
            "Review Comment"
        )

    def test_rating_widget_attributes(self):
        """Check that the rating field uses a select dropdown with correct attributes."""
        form = ReviewForm()
        self.assertEqual(
            form.fields["rating"].widget.attrs["class"],
            "form-select"
        )
        self.assertEqual(
            form.fields["rating"].widget.attrs["aria-label"],
            "Select Rating"
        )
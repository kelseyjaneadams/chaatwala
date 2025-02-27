from django.test import SimpleTestCase
from django.urls import reverse, resolve
from reviews.views import submit_review, edit_review, delete_review


class TestReviewUrls(SimpleTestCase):
    """Test that review URLs resolve to the correct views."""

    def test_submit_review_url_resolves(self):
        """Test that the 'submit_review' URL maps to the correct view."""
        url = reverse("submit_review")
        self.assertEqual(resolve(url).func, submit_review)

    def test_edit_review_url_resolves(self):
        """Test that the 'edit_review' URL maps to the correct view."""
        url = reverse("edit_review", args=[1])
        self.assertEqual(resolve(url).func, edit_review)

    def test_delete_review_url_resolves(self):
        """Test that the 'delete_review' URL maps to the correct view."""
        url = reverse("delete_review", args=[1])
        self.assertEqual(resolve(url).func, delete_review)

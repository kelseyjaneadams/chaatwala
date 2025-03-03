from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from reviews.models import Review


class ReviewViewsTest(TestCase):
    """Test case for the Reviews app views."""

    def setUp(self):
        """Set up a test client, user, and sample reviews."""
        self.client = Client()
        self.user = User.objects.create_user(
            username="testuser", password="password123"
        )
        self.other_user = User.objects.create_user(
            username="otheruser", password="password123"
        )
        self.client.login(username="testuser", password="password123")

        self.approved_review = Review.objects.create(
            user=self.user,
            rating=5,
            comment="Great experience!",
            status="approved"
        )

        self.pending_review = Review.objects.create(
            user=self.user,
            rating=4,
            comment="Pending review",
            status="pending"
        )

    def test_menus_view(self):
        """Test that the menus page loads and displays reviews correctly."""
        response = self.client.get(reverse("menus"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "bookings/menus.html")

        self.assertContains(response, "Great experience!")
        self.assertContains(response, "Pending review")

    def test_submit_review_valid(self):
        """Test that a logged-in user can submit a review successfully."""
        form_data = {
            "rating": 5,
            "comment": "Excellent service!"
        }
        response = self.client.post(
            reverse("submit_review"), data=form_data, follow=True
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(
            response,
            "Your review is pending approval."
        )
        self.assertEqual(Review.objects.count(), 3)
        self.assertEqual(Review.objects.last().status, "pending")

    def test_submit_review_invalid(self):
        """Test that submitting an empty review shows an error."""
        form_data = {}
        response = self.client.post(
            reverse("submit_review"), data=form_data, follow=True
        )

        self.assertEqual(response.status_code, 200)
        messages = list(response.context["messages"])
        self.assertTrue(
            any(
                "There was an error submitting your review." in str(msg)
                for msg in messages
            )
        )

    def test_edit_review_success(self):
        """Test that a logged-in user can edit their own review."""
        edit_url = reverse("edit_review", args=[self.pending_review.id])
        form_data = {
            "rating": 3,
            "comment": "Updated comment"
        }
        response = self.client.post(edit_url, data=form_data, follow=True)

        self.pending_review.refresh_from_db()
        self.assertEqual(response.status_code, 200)
        self.assertContains(
            response,
            "Your review has been updated successfully."
        )
        self.assertEqual(self.pending_review.comment, "Updated comment")

    def test_edit_review_unauthorized(self):
        """Test that a user cannot edit someone else's review."""
        self.client.logout()
        self.client.login(username="otheruser", password="password123")

        edit_url = reverse("edit_review", args=[self.pending_review.id])
        response = self.client.post(edit_url, follow=True)

        self.assertEqual(response.status_code, 404)

    def test_delete_review_success(self):
        """Test that a logged-in user can delete their own review."""
        delete_url = reverse("delete_review", args=[self.pending_review.id])
        response = self.client.post(delete_url, follow=True)

        self.assertEqual(response.status_code, 200)
        self.assertContains(
            response,
            "Your review has been deleted."
        )
        self.assertFalse(
            Review.objects.filter(id=self.pending_review.id).exists()
        )

    def test_delete_review_unauthorized(self):
        """Test that a user cannot delete someone else's review."""
        self.client.logout()
        self.client.login(username="otheruser", password="password123")

        delete_url = reverse("delete_review", args=[self.pending_review.id])
        response = self.client.post(delete_url, follow=True)

        self.assertEqual(response.status_code, 404)
        self.assertTrue(
            Review.objects.filter(id=self.pending_review.id).exists()
        )

    def test_unauthenticated_access_redirects(self):
        """Ensure unauthenticated users are redirected from protected views."""
        self.client.logout()

        protected_urls = [
            reverse("submit_review"),
            reverse("edit_review", args=[self.pending_review.id]),
            reverse("delete_review", args=[self.pending_review.id]),
        ]

        for url in protected_urls:
            response = self.client.get(url, follow=True)
            self.assertRedirects(
                response,
                f"/accounts/login/?next={url}"
            )

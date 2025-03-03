from django.test import TestCase
from django.contrib.auth.models import User
from reviews.models import Review
from datetime import datetime
from django.core.exceptions import ValidationError


class ReviewModelTest(TestCase):
    """Test case for the Review model."""

    def setUp(self):
        """Set up a user and a review instance before each test."""
        self.user = User.objects.create_user(
            username="testuser",
            password="password123"
        )

        self.review = Review.objects.create(
            user=self.user,
            rating=5,
            comment="Great food!",
            status=Review.STATUS_APPROVED,
            created_on=datetime(2025, 3, 15, 12, 0, 0)
        )

    def test_review_str_representation(self):
        """Test the __str__ method of the Review model."""
        expected_str = "Review by testuser with rating 5"
        self.assertEqual(str(self.review), expected_str)

    def test_review_default_status_is_pending(self):
        """Test that the default status of a review is 'PENDING'."""
        new_review = Review.objects.create(
            user=self.user,
            rating=4,
            comment="Nice ambiance!"
        )
        self.assertEqual(new_review.status, Review.STATUS_PENDING)

    def test_approved_review_resets_to_pending_on_update(self):
        """Test that updating an approved review changes status
            to 'PENDING'."""
        self.review.comment = "Updated review text"
        self.review.save()

        self.review.refresh_from_db()
        self.assertEqual(self.review.status, Review.STATUS_PENDING)

    def test_review_comment_max_length(self):
        """Test that the comment field enforces a maximum length
            of 500 characters."""
        long_comment = "A" * 501

        review = Review(
            user=self.user,
            rating=3,
            comment=long_comment
        )

        with self.assertRaises(ValidationError) as context:
            review.full_clean()

        self.assertIn("comment", context.exception.message_dict)

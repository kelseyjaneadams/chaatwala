from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth.models import User


class Review(models.Model):
    """
    Stores a single review entry related to :model:`auth.User`.
    Each review includes a unique ID, a rating, an optional comment,
    and the date the review was created. The review is associated with
    a specific user who created it.
    """
    review_id = models.CharField(
        primary_key=True,
        max_length=50,
        editable=False
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    rating = models.IntegerField()
    comment = models.TextField(
        blank=True,
        null=True
    )
    review_date = models.DateTimeField(
        auto_now_add=True
    )

    def clean(self):
        """
        Validates the comment field to ensure it does not exceed
        the maximum allowed character length of 500.
        """
        super().clean()
        if self.comment and len(self.comment) > 500:
            raise ValidationError("Comment cannot exceed 500 characters.")

    def save(self, *args, **kwargs):
        """
        Overrides save method to generate a unique review ID
        prefixed with 'REV' and starting from 1.
        """
        if not self.review_id:
            last_review = Review.objects.order_by('id').last()
            next_id = last_review.id + 1 if last_review else 1
            self.review_id = f"REV{next_id}"
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Review {self.review_id} by {self.user.username}"

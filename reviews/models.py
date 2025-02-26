from django.db import models
from django.contrib.auth.models import User


class Review(models.Model):
    """ Model representing user reviews. """

    RATING_CHOICES = (
        (1, "1 - Very Poor"),
        (2, "2 - Poor"),
        (3, "3 - Average"),
        (4, "4 - Good"),
        (5, "5 - Excellent"),
    )

    STATUS_PENDING = "pending"
    STATUS_APPROVED = "approved"

    STATUS_CHOICES = (
        (STATUS_PENDING, "Pending"),
        (STATUS_APPROVED, "Approved"),
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    rating = models.IntegerField(choices=RATING_CHOICES)
    comment = models.TextField(blank=False)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default=STATUS_PENDING
    )

    def save(self, *args, **kwargs):
        """ If an approved review is updated, reset status to pending. """
        if self.pk:
            original_review = Review.objects.get(pk=self.pk)
            if original_review.status == self.STATUS_APPROVED:
                self.status = self.STATUS_PENDING

        super().save(*args, **kwargs)

    def __str__(self):
        """ String representation of the review. """
        return f"Review by {self.user.username} with rating {self.rating}"
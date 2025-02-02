from django.db import models
from django.contrib.auth.models import User


class Review(models.Model):
    RATING_CHOICES = (
        (1, "1 - Very Poor"),
        (2, "2 - Poor"),
        (3, "3 - Average"),
        (4, "4 - Good"),
        (5, "5 - Excellent"),
    )

    STATUS_CHOICES = (
        ("pending", "Pending"),
        ("approved", "Approved"),
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    rating = models.IntegerField(choices=RATING_CHOICES)
    comment = models.TextField(blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default="pending"
    )

    def __str__(self):
        return (
            f"Review by {self.user.username} "
            f"with rating {self.rating}"
        )
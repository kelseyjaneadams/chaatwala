from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Review(models.Model):
    """
    Stores a single review entry related to :model:`auth.User`.
    Each review includes a unique ID, a rating, an optional comment,
    and the date the review was created. The review is associated with
    a specific user who created it.
    """
    review_id = models.CharField(
        primary_key=True,
        max_length=50
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    # add max character length?
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
        the maximum allowed character length of 1000.
        """
        super().clean()
        if self.comment and len(self.comment) > 500: 
            raise ValidationError("Comment cannot exceed 1000 characters.")
    

    def __str__(self):
        return f"Review {self.review_id} by {self.user.username}"
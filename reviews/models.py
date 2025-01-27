from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_save
from django.dispatch import receiver


class Review(models.Model):
    review_id = models.CharField(
        primary_key=True,
        max_length=50,
        editable=False,
        unique=True
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField(blank=True, null=True)
    review_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review {self.review_id} by {self.user.username}"


@receiver(pre_save, sender=Review)
def set_review_id(sender, instance, **kwargs):
    if not instance.review_id:
        last_review = Review.objects.order_by('review_id').last()
        next_id = int(last_review.review_id.replace("REV", "")) + 1 if last_review else 1
        instance.review_id = f"REV{next_id:03d}"

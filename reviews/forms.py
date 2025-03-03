from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):
    """
    Form for users to submit a review.
    Uses Crispy Forms for better styling and validation.
    """

    comment = forms.CharField(
        max_length=500,
        widget=forms.Textarea(
            attrs={
                "class": "form-control",
                "rows": 3,
                "placeholder": (
                    "Write your review here... (Max 500 characters)"
                ),
                "aria-label": "Review Comment",
            }
        ),
        required=True,
        strip=True,
    )

    class Meta:
        model = Review
        fields = ["rating", "comment"]

        widgets = {
            "rating": forms.Select(
                choices=Review.RATING_CHOICES,
                attrs={
                    "class": "form-select",
                    "aria-label": "Select Rating",
                }
            ),
        }

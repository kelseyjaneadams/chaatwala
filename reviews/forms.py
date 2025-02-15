from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):
    """
    Form for users to submit a review.
    Uses Crispy Forms for better styling and validation.
    """

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
            "comment": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 3,
                    "placeholder": "Write your review here...",
                    "aria-label": "Review Comment",
                }
            ),
        }

    def clean_comment(self):
        """
        Ensure the review comment is not empty after stripping whitespace.
        """
        comment = self.cleaned_data.get("comment", "").strip()
        if not comment:
            raise forms.ValidationError("Your review comment cannot be empty.")
        return comment
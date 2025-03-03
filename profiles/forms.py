from django import forms
from .models import Profile


class ProfileImageForm(forms.ModelForm):
    """
    Form for updating the profile image, ensuring proper file input display.
    """
    image = forms.ImageField(
        label="Upload New Profile Picture",
        widget=forms.FileInput(attrs={"class": "form-control-file"})
    )

    class Meta:
        model = Profile
        fields = ["image"]

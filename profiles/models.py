from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Profile(models.Model):
    """
    Stores additional information about users, such as profile images.
    Each profile is linked to a single user from the User model.
    """
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    ) 

    image = CloudinaryField(
        "image",
        default="profile_pics/default"
    )

    def __str__(self):
        return f"{self.user.username}'s Profile"

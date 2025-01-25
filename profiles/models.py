from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    """
    Stores additional information about users, such as profile images.
    Each profile is linked to a single user from the User model.
    """
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )  # Links Profile to a single User
    image = models.ImageField(
        upload_to='profile_pics/',
        default='profile_pics/default.jpg'
    )  # Handles profile images

    def __str__(self):
        return f"{self.user.username}'s Profile"
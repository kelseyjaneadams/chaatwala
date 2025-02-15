from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Profile

@receiver(post_save, sender=User)
def create_or_update_profile(sender, instance, created, **kwargs):
    """
    Signal to create a Profile whenever a new User is created.
    Assigns a default Cloudinary profile image if none is provided.
    Ensures existing users without profiles get one.
    """
    profile, created = Profile.objects.get_or_create(user=instance)

    if created and not profile.image:
        profile.image = "profile_pics/default"
        profile.save()

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    """
    Ensures Profile updates whenever the User model is updated.
    """
    if hasattr(instance, 'profile'):
        instance.profile.save()
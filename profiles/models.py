from django.db import models
from django.contrib.auth.models import User


# This module defines the Profile model for the application, extending the default User model.


class Profile(models.Model):
    """
    Profile model extending the default User model. Each user can have one profile,
    represented by the one-to-one relationship between User and Profile.
    Returns:
        str: A string representation of the model, which is the username of the associated user.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # The user associated with this profile.
    favorite_city = models.CharField(max_length=64, blank=True)
    # A user's favorite city. It's an optional field.

    def __str__(self):
        return self.user.username

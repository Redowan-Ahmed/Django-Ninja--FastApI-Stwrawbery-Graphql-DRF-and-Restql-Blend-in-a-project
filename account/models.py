from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator

# Create your models here.
class CustomUser(AbstractUser):
    phoneNumberRegex = RegexValidator(
        regex=r"^\+?1?\d{8,15}$", message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(
        validators=[phoneNumberRegex], max_length=16, default=8801632398271
    )
    profile_picture = models.ImageField(
        upload_to='user-profile-images', default='/static/media/logo.png')


    def __str__(self) -> str:
        return self.username
"""
USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()
"""
from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.core.validators import validate_email, RegexValidator
from planner_app.managers.user_manager import UserManager

password_validator = RegexValidator(
    regex=r'^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{6,}$',
    message="Password must have at least 6 characters, 1 letter, 1 number, and 1 special character."
)


class User(AbstractBaseUser):
    email = models.EmailField(unique=True, validators=[validate_email])
    password = models.CharField(max_length=128, validators=[password_validator])
    PROFILE_CHOICES = (
        ('user', 'User'),
        ('trainer', 'Trainer'),
    )
    profile = models.CharField(max_length=7, choices=PROFILE_CHOICES, default='user')

    objects = UserManager()

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ['profile']

    def __str__(self):
        return self.email

import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models
from .managers import UserManager


class User(AbstractUser):
    uuid = models.UUIDField(
        default=uuid.uuid4, editable=False, unique=True, db_index=True
    )
    email = models.EmailField(unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    objects = UserManager

    def __str__(self):
        return self.get_username()

    def save(self, *args, **kwargs):
        if self.email:
            self.username = self.email
        return super().save(*args, **kwargs)

from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class Pet(models.Model):
    owner = models.ManyToManyField(User)

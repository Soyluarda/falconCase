from django.contrib.auth.models import AbstractUser
from django.db import models
from riot.models import Char

class ExtendedUser(AbstractUser):
    char = models.ManyToManyField(Char,null=True,blank=True)


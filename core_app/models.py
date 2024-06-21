from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class User(AbstractUser):
  user_abbreviation = models.CharField(max_length=50, blank = False, unique = True) 
  email = models.EmailField(unique=True)
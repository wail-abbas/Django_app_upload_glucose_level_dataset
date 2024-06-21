from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class User(AbstractUser):
  user_abbreviation = models.CharField(max_length=50, blank = False, unique = True) 
  email = models.EmailField(unique=True)
  address = models.CharField(max_length=50, blank = True, unique = False)
  birthdate = models.CharField(max_length=50, blank = True, unique = False)
  mobile_number = models.CharField(max_length=50, blank = True, unique = False)
  user_abbreviation = models.CharField(max_length=50, blank = False, unique = True)
import hashlib

from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import UserManager, PermissionsMixin
from django.db import models
from django.utils import timezone
from utils.ReadableDateTime import generate_readable_date_time


class User(AbstractBaseUser, PermissionsMixin):
    """
    Use model to store all user information
    """
    first_name = models.TextField(default="")
    last_name = models.TextField(default="")
    phone_number = models.TextField(null=True)  # Used as the entry point of the account or username field
    email = models.TextField(primary_key=True, null=False)  # To store email address
    password = models.TextField(null=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.first_name + " " + self.last_name + "->" + self.email

    def get_full_name(self):
        return self.first_name + " " + self.last_name

    def get_phone_number(self):
        return self.phone_number


class Profile(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    age = models.IntegerField(max_length=4)
    sex = models.CharField(max_length=4)
    salary = models.CharField(max_length=8)


class Employee(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=200)
    age = models.IntegerField(max_length=2)
    salary = models.CharField(max_length=8)


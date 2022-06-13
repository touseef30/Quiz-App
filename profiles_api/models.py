from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from django.conf import settings

# Models


class UserProfileManager(BaseUserManager):
    """ Manager for user Profile"""

    def create_user(self, email,name=None, password=None,is_staff=False):
        """Create a new user profile"""
        if not email:
            raise ValueError('No email provided')

        email = self.normalize_email(email)
        user = self.model(email=email,name=name,is_staff=is_staff)

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email,name="", password="",is_staff=False):
        """Create new super User"""
        user = self.create_user(email,name, password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database model for users in the system"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_enabled = models.BooleanField(default=True)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'

    def get_full_name(self):
        """Full Name"""
        return self.name

    def get_short_name(self):
        """Short Name"""
        return self.name

    def __str__(self):
        """String"""
        return self.email


class EmailToken(models.Model):
    token = models.CharField(max_length=255)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    usetype = models.CharField(max_length=255)

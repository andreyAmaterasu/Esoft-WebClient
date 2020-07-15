from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.utils import timezone
from .managers import CustomUserManager

class Useraccount(AbstractBaseUser):
    login = models.CharField(primary_key=True, max_length=50)
    password = models.CharField(max_length=50)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'login'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.login

# class Useraccount(AbstractBaseUser):
#     login = models.CharField(primary_key=True, max_length=50)
#     password = models.CharField(max_length=50)
#     date_joined = models.DateTimeField(verbose_name="date joined", auto_now_add=True)
#     last_login = models.DateTimeField(verbose_name="lastlogin", auto_now=True)
#     is_active = models.BooleanField(default=True)

#     USERNAME_FIELD = 'login'
#     REQUIRED_FIELDS = ['password',]

#     class Meta:
#         db_table = 'useraccount'
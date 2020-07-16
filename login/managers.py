from django.db import models
from django.contrib.auth.models import BaseUserManager, PermissionsMixin

class UserManager(BaseUserManager):

    def get_by_natural_key(self, login_):
       return self.get(login=login_)
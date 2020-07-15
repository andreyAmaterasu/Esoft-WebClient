from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import ugettext_lazy as _
class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """

    def get_by_natural_key(self, login):
        return self.get(login=login)
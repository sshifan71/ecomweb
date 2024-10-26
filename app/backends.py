from .models import *
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model


class EmailOrUsernameBackend(ModelBackend):
    """
    Custom authentication backend to allow login with either email or username.
    """
    def authenticate(self, request, username=None, password=None, **kwargs):
        UserModel = get_user_model()
        try:
            # Try to get the user by email if username looks like an email
            if '@' in username:
                user = UserModel.objects.get(email=username)
            else:
                # Otherwise, try to get the user by username
                user = UserModel.objects.get(username=username)
        except UserModel.DoesNotExist:
            return None

        if user.check_password(password) and self.user_can_authenticate(user):
            return user
        return None

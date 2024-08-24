from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
# Create your models here.
# 1. Override the email field
# 2. Override the username field
# 3. A user manager
# 4. Register the User model with Django admin
class UserManager(BaseUserManager):
    def create_user(self, email, password):
        if not email:
            raise ValueError("Users must have an email")
        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.save(using=self._db)
        return user
        

    def create_superuser(self, email, password, username=None):
        user = self.create_user(email, password)

        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user

class User(AbstractUser):
    email = models.EmailField(unique=True, max_length=255)
    username = models.CharField(unique=True, max_length=10)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()




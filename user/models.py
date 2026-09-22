from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.utils import timezone

class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("User must have an email!!")

        email = self.normalize_email(email)

        user = self.model(
            email=email,
            **extra_fields
        )

        user.set_password(password)
        user.save(using=self._db)

        return user



class CustomUser(AbstractBaseUser):

    
    email = models.EmailField(unique=True, max_length=255)
    city = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    surename = models.CharField(max_length=100, blank=True, null=True)
    is_active = models.BooleanField(default=True)

    date_joined = models.DateTimeField(
        default=timezone.now
    )


    objects = UserManager()

    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.email





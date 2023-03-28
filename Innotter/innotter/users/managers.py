from django.contrib.auth.base_user import BaseUserManager
from django.db import transaction


class CustomUserManager(BaseUserManager):
    def _create_user(self, username, email, password, **extra_fields):
        if not email:
            raise ValueError('The given email must be set')
        try:
            with transaction.atomic():
                user = self.model(username=username,
                                  email=email, **extra_fields)
                user.set_password(password)
                user.save(using=self._db)
                return user
        except:
            ValueError('Some error')

    def create_user(self, username, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        extra_fields.setdefault('role', 'user')
        return self._create_user(username, email,
                                 password=password, **extra_fields)

    def create_superuser(self, username, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('role', 'admin')
        return self._create_user(username, email,
                                 password=password, **extra_fields)

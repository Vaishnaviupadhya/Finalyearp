# models.py
# from django.contrib.auth.models import AbstractUser
# from django.db import models

# class CustomUser(AbstractUser):
#     USER_TYPE_CHOICES = [
#         (0, 'Patient'),
#         (1, 'Doctor'),
#     ]

#     # Additional fields
#     type = models.IntegerField(choices=USER_TYPE_CHOICES, default=0)
#     #email = models.EmailField(unique=True)
#     name = models.CharField(max_length=255,default='')
#     username=None
#     # Add related_name to avoid clashes with auth.User
#     groups = models.ManyToManyField(
#         'auth.Group',
#         verbose_name='groups',
#         blank=True,
#         related_name='customuser_set',
#         related_query_name='customuser',
#     )
#     user_permissions = models.ManyToManyField(
#         'auth.Permission',
#         verbose_name='user permissions',
#         blank=True,
#         related_name='customuser_set',
#         related_query_name='customuser',
#     )

# models.py
# models.py
# from django.contrib.auth.models import BaseUserManager
# from django.db import models

# class CustomUserManager(BaseUserManager):
#     def create_user(self, email, password=None, **extra_fields):
#         if not email:
#             raise ValueError('The Email field must be set')
#         email = self.normalize_email(email)
#         user = self.model(email=email, **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_superuser(self, email, password=None, **extra_fields):
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', True)
#         return self.create_user(email, password, **extra_fields)

# class CustomUser(AbstractUser):
#     USER_TYPE_CHOICES = [
#         (0, 'Patient'),
#         (1, 'Doctor'),
#     ]

#     # Additional fields
#     type = models.IntegerField(choices=USER_TYPE_CHOICES, default=0)
#     email = models.EmailField(unique=True)
#     name = models.CharField(max_length=255, blank=True)
#     objects = CustomUserManager()

#     #Remove the 'username' field
#     username = None

#     # Add related_name to avoid clashes with auth.User
#     groups = models.ManyToManyField(
#         'auth.Group',
#         verbose_name='groups',
#         blank=True,
#         related_name='customuser_set',
#         related_query_name='customuser',
#     )
#     user_permissions = models.ManyToManyField(
#         'auth.Permission',
#         verbose_name='user permissions',
#         blank=True,
#         related_name='customuser_set',
#         related_query_name='customuser',
#     )
  #  def __str__(self):
       # return self.email  # Assuming you want to represent the user by their email address
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

class CustomUser(AbstractBaseUser, PermissionsMixin):
    USER_TYPE_CHOICES = [
        (0, 'Patient'),
        (1, 'Doctor'),
    ]

    email = models.EmailField(unique=True)
    name = models.CharField(max_length=255, default='')
    type = models.IntegerField(choices=USER_TYPE_CHOICES, default=0)

    objects = CustomUserManager()

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'type']

    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        related_name='custom_users_groups',  # Add a unique related_name
        related_query_name='customuser_group',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        related_name='custom_users_permissions',  # Add a unique related_name
        related_query_name='customuser_permission',
    )

    def __str__(self):
        return self.email


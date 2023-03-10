from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils.translation import gettext_lazy as _


# Create your models here.

class UserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """Create and save a regular User with the given email and password."""
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class User(AbstractUser):
    """User model."""

    username = None

    last_name = models.CharField(max_length=35)
    email = models.EmailField(_('email address'), unique=True)
    phone = None  # models.CharField(max_length=35)
    first_name = models.CharField(max_length=35)
    # models.ImageField(upload_to='seller_profile_image', blank=True, null=True)
    image = None
    address = None  # models.CharField(max_length=255,blank=True, null=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()


class Address(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=30, null=True, blank=True)
    phone = models.CharField(max_length=11, null=True, blank=True)
    city = models.CharField(max_length=20, null=True, blank=True)
    thana = models.CharField(max_length=20, null=True, blank=True)
    postal_code = models.CharField(max_length=20, null=True, blank=True)
    detail_address = models.TextField(max_length=100, null=True, blank=True)

    def __str__(self) -> str:
        return self.detail_address

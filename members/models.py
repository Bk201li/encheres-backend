from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

# Create your models here.

class UserManager(BaseUserManager):
    use_in_migrations = True
    def create_user(self, email, password=None, is_admin=False, is_staff=False, is_active=True):       
        user = self.model(
            email=self.normalize_email(email)
        )

        if password:
            user.set_password(password)
        else:
            user.set_unusable_password()
        user.admin = is_admin
        user.staff = is_staff
        user.active = is_active
        user.save(using=self._db)
        return user
        
    def create_superuser(self, email, password, **extra_fields):
        user = self.model(
            email=self.normalize_email(email)
        )

        user.set_password(password)
        user.admin = True
        user.staff = True
        user.active = True
        user.save(using=self._db)
        return user

class User(AbstractUser):
    first_name = models.CharField(max_length=255, blank=True, default='')
    last_name = models.CharField(max_length=255, blank=True, default='')
    birth_date = models.DateField(null=True)
    phone_number = models.CharField(max_length=255, blank=True, default='')
    email = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    image = models.ImageField(upload_to="images/", null=True)
    area = models.CharField(max_length=255, blank=True, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    username = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = UserManager()

    def __str__(self):
        return self.email

    class Meta:
        ordering = ["-updated_at"]

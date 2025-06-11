from django.contrib.auth.models import AbstractUser
from django.db import models

from django.db.models import TextChoices
from django.db.models.fields import CharField

class UploadedFile(models.Model):

    name = models.CharField(max_length=100, blank=True, null=True)
    file = models.FileField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name if self.name else "Unnamed File"


class User(AbstractUser):
    class RoleType(TextChoices):
        USER = 'user', 'User'
        ADMIN = 'admin', 'Admin'
        SUPERADMIN = 'super admin', 'Super Admin'

    email = models.EmailField(unique=True)
    phone = CharField(max_length=18, unique=True)
    role = CharField(max_length=60 , choices=RoleType , default=RoleType.USER)

    def __str__(self):
        return self.username


# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-= Parking Models =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=



















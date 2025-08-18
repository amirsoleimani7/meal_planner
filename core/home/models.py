from django.db import models
from django.contrib.auth.models import User , AbstractUser
from .manager import UserManager

class GFG(AbstractUser):
    phone = models.CharField(max_length=12, unique=True)

    USERNAME_FIELD = "phone"
    REQUIRED_FIELDS = []

    objects = UserManager()


class Recipe(models.Model):
    user = models.ForeignKey(GFG , on_delete=models.SET_NULL , null=True ,blank=True)
    day = models.CharField(max_length=100 , default='something')
    name = models.CharField(max_length=100 , default='something')
    description = models.TextField(default='something')
    
    def __str__(self):
        return self.name
    





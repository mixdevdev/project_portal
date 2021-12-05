from typing import Annotated
from django.db import models
from django.contrib.auth.models import  AbstractUser

# Create your models here.

class User(AbstractUser):
    name_enterprise=models.CharField(max_length=200,default=' ',verbose_name='Nom entreprise')
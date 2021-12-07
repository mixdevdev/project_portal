from typing import Annotated
from django.db import models
from django.contrib.auth.models import  AbstractUser

# Create your models here.

class User(AbstractUser):
    name_enterprise=models.CharField(max_length=200,default=' ',verbose_name='Nom entreprise')
    nif_stat=models.CharField(max_length=200,default=' ',verbose_name='Nif-Stat')
    is_recruiter=models.BooleanField(default=False,verbose_name='Est un recruteur')
    is_trainer=models.BooleanField(default=False,verbose_name='Est un formateur')


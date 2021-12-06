from django.db import models
from datetime import datetime,date
from registration.models import User

# Create your models here.

class Administration(models.Model):
    coverage_photo=models.ImageField(upload_to='portaljob_activity')

class Recruitment_info(models.Model):
    name=models.CharField(max_length=200,default='')
    pub_date=models.DateField('date de publication',default='')
    user_id=models.ForeignKey(User, on_delete=models.CASCADE)
    end_recruitment_date=models.DateField('Fin de recruitement',default='')
    description=models.TextField('Description on the job',default='')
    def __str__(self):
        return self.name

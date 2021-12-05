from django.db import models
from datetime import datetime,date
from registration.models import User

# Create your models here.

class Recruitment_info(models.Model):
    name=models.CharField(max_length=200,default='')
    pub_date=models.DateField('date de publication')
    user_id=models.ForeignKey(User, on_delete=models.CASCADE)
    end_recruitment_date=models.DateField('Fin de recruitement',default='')
    description=models.TextField('Description on the job',default='')
    def __str__(self):
        return self.name

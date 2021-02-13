from django.db import models
from datetime import datetime
# Create your models here.
class Agent(models.Model):
    name = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='agents/%Y/%m/%d')
    description = models.TextField(blank=True)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    skype = models.CharField(max_length=30)
    facebook = models.CharField(max_length=100)
    twitter = models.CharField(max_length=100)
    hire_date = models.DateTimeField(default=datetime.now,blank=True)

    def __str__(self):
        return self.name
    
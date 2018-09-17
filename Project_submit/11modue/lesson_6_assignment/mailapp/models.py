from django.db import models
from django.contrib.auth.models import User

class Mail(models.Model):
    name = models.CharField(max_length=128)
    amount = models.IntegerField(blank = True)
    created_date = models.DateTimeField(auto_now =True)

# Create your models here.

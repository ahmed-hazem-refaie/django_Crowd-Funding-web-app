from django.db import models
from login.models import User

# Create your models here.

class DataAdd (models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    birthdate= models.DateTimeField(blank=True,null=True)
    country=models.CharField(max_length=40,blank=True)
    facebookprofile=models.TextField(default=' ',blank=True)


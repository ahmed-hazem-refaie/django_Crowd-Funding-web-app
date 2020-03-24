from django.db import models
from django.core.validators import RegexValidator
from  django.core import  validators
from datetime import  datetime
from django import  forms
import  uuid


class User (models.Model):
    f_name=models.CharField(max_length=90,blank=False)
    l_name=models.CharField(blank=False,max_length=90)
    email=models.EmailField(blank=False,max_length=254,unique=True)
    password=models.CharField(blank=False,max_length=30)
    phone_regex = RegexValidator(regex=r'^(010|011|012)', message="Phone number must be entered in the format: '01234567890'. Up to 11 digits allowed.")
    phone=models.CharField(  validators=[
        RegexValidator('^(010|011|012)[0-9]{8}$',
            message='number must be 01112342342',

        ), ],max_length=11)
    profile_pic = models.ImageField(upload_to=f"login/static/{uuid.uuid4()}",blank=True)

    gender = models.CharField(default=None,blank=False,
        max_length=2,
        choices= (
        ('F', 'female'),
        ('M','male'),
    )
    )
    state = models.CharField(default='D',blank=False,
                              max_length=2,
                              choices=(
                                  ('A', 'active'),
                                  ('D', 'disable'),
                              )
                              )

    code=models.CharField(default=0,max_length=90)
    datetime=models.DateTimeField(auto_now_add=True,null=True)





#
#
#
# from author.models import Author
#
# # Create your models here.
# class Book(models.Model):
#
#     title=models.CharField(max_length=100)
#     author_id=models.ForeignKey(Author,on_delete=models.CASCADE)
#     details = models.CharField(max_length=200)
#     price=models.IntegerField(null=True)
#     # upload_img = models.ImageField(upload_to='images/')

# import datetime
# lastplus = q.get()
# if lastplus.date < datetime.datetime.now()-datetime.timedelta(seconds=20):
#     print "Go"
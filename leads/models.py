from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
#from .models import User,UserProfile
# Create your models here.

class User(AbstractUser):
    is_organisor=models.BooleanField(default=True)
    is_agent=models.BooleanField(default=False)

class UserProfile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
 
    def __str__(self):
        return self.user.username

class LeadModel(models.Model):
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    age=models.IntegerField()
    organisation=models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    agent=models.ForeignKey('AgentModel',null=True,blank=True,on_delete=models.SET_NULL)
    Category=models.ForeignKey("CategoryModel",null=True,blank=True,on_delete=models.SET_NULL)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"



class AgentModel(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    organisation=models.ForeignKey(UserProfile,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user.email)

class CategoryModel(models.Model):
    name=models.CharField(max_length=30)
    organisation=models.ForeignKey(UserProfile,on_delete=models.CASCADE)

    def __str__(self):
        return self.name


def post_user_created_signal(sender,instance,created,**kwargs):
    if created:
        UserProfile.objects.create(user=instance)

post_save.connect(post_user_created_signal,sender=User)
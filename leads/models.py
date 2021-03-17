from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    pass

class UserProfile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
 
    def __str__(self):
        return self.user.username

class LeadModel(models.Model):
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    age=models.IntegerField()
    agent=models.ForeignKey('AgentModel',on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"



class AgentModel(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    organisation=models.ForeignKey(UserProfile,on_delete=models.CASCADE)

    def __str__(self):
        return self.email
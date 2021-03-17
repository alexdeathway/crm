'''
from django.db.models.signals import post_save
from .models import User,UserProfile


def post_user_created_signal(sender,instance,created,**kwargs):
    print("got that")
    if created:
        UserProfile.objects.create(user=instance)

post_save.connect(post_user_created_signal,sender=User)
'''
from django import forms
from django.contrib.auth import get_user_model
from .models import LeadModel
from django.contrib.auth.forms import UserCreationForm,UsernameField

User=get_user_model()


class LeadCreationForm(forms.ModelForm):
 
    class Meta:
        model=LeadModel
        fields=[
            "first_name",
            "last_name",
            "age",
            "agent",
        ]


class AgentCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username",)
        field_classes = {'username': UsernameField}
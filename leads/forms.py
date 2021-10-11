from django import forms
from django.contrib.auth import get_user_model
from django.db.models.query import QuerySet
from django.http import request
from .models import AgentModel, LeadModel
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


class UserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username",)
        field_classes = {'username': UsernameField}

class AssignAgentForm(forms.Form):
    agents=forms.ModelChoiceField(queryset=AgentModel.objects.none())

    def __init__(self,*args, **kwargs):
        request=kwargs.pop("request")
        agents=AgentModel.objects.filter(organisation=request.user.userprofile)
        super(AssignAgentForm,self).__init__(*args,**kwargs)
        self.fields["agents"].queryset=agents
        
class CategoryUpdateForm(forms.ModelForm):
      class Meta:
        model=LeadModel
        fields=[
            "category",
        ]      
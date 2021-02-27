from django import forms
from .models import LeadModel

class LeadCreationForm(forms.ModelForm):
 
    class Meta:
        model=LeadModel
        fields=[
            "first_name",
            "last_name",
            "age",
            "agent",
        ]    
from django import forms
from leads.models import AgentModel

class AgentModelForm(forms.ModelForm):
    class Meta:
        model=AgentModel
        fields=[
            'user',
            
        ]
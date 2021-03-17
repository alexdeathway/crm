from django.contrib import admin
from .models import LeadModel,AgentModel,UserProfile
# Register your models here.

admin.site.register(LeadModel)
admin.site.register(AgentModel)
admin.site.register(UserProfile)
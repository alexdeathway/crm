from django.contrib import admin
from .models import LeadModel,AgentModel,UserProfile,User
# Register your models here.

admin.site.register(LeadModel)
admin.site.register(AgentModel)
admin.site.register(UserProfile)
admin.site.register(User)
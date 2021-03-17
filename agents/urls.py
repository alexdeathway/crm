from django.urls import path
from .views import AgentListView,AgentCreatView

app_name='agents'

urlpatterns=[
    path('',AgentListView.as_view(),name="agents"),
    path('create/',AgentCreatView.as_view(),name="agentcreate"),

]
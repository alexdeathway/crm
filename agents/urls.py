from django.urls import path
from .views import (
                    AgentListView,
                    AgentCreatView,
                    AgentDetailView,
                    AgentUpdateView,
                    AgentDeleteView
                    )



app_name='agents'

urlpatterns=[
    path('',AgentListView.as_view(),name="agents"),
    path('create/',AgentCreatView.as_view(),name="agentcreate"),
    path("<int:pk>/",AgentDetailView.as_view(),name="agentdetail"),
    path("<int:pk>/update/",AgentUpdateView.as_view(),name="agentupdate"),
    path("<int:pk>/delete/",AgentDeleteView.as_view(),name="agentdelete"),

]
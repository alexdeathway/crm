from django.urls import path
from .views import (
                    index,
                    leadlist,
                    CreateLead
                    )        

urlpatterns=[
    path("",index),
    path("leadlist/",leadlist),
    path("create/",CreateLead)
]
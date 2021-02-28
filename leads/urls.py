from django.urls import path
from .views import (
                    index,
                    LeadList,
                    LeadCreate,
                    LeadDetail,
                    LeadUpdate,
                    )        

urlpatterns=[
    path("",index),
    path("leadlist/",LeadList,name="leadlist"),
    path("create/",LeadCreate,name="leadcreate"),
    path("<int:pk>",LeadDetail),
    path("<int:pk>/update",LeadUpdate)
]
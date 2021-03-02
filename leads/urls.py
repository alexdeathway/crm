from django.urls import path
from .views import (
                    index,
                    LeadList,
                    LeadCreate,
                    LeadDetail,
                    LeadUpdate,
                    LeadDelete,
                    )        

urlpatterns=[
    path("",index),
    path("leadlist/",LeadList,name="leadlist"),
    path("create/",LeadCreate,name="leadcreate"),
    path("<int:pk>/",LeadDetail,name="leaddetail"),
    path("<int:pk>/update/",LeadUpdate,name="leadupdate"),
    path("<int:pk>/delete/",LeadDelete,name="leaddelete")
]
from django.urls import path
from .views import (
                    index,
                    LeadList,
                    LeadCreate,
                    LeadDetail,
                    LeadUpdate,
                    LeadDelete,
                    LandingPageView,
                    LeadListView,
                    LeadDetailView,
                    LeadCreateView,
                    LeadUpdateView,
                    LeadDeleteView,
                    )        

app_name="leads"

urlpatterns=[
    path("",LeadListView.as_view(),name="leadlist"),
    path("create/",LeadCreateView.as_view(),name="leadcreate"),
    path("<int:pk>/",LeadDetailView.as_view(),name="leaddetail"),
    path("<int:pk>/update/",LeadUpdateView.as_view(),name="leadupdate"),
    path("<int:pk>/delete/",LeadDeleteView.as_view(),name="leaddelete")
]
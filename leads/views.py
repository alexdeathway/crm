from django.shortcuts import render
from django.http import HttpResponse
from .models import LeadModel
from .forms import LeadCreationForm
# Create your views here.


def index(request):
    print(request)
    return HttpResponse("Received")

def leadlist(request):
     leads=LeadModel.objects.all()
     context={
         "leads":leads
     }
     return render(request,"leads/leads_list.html",context)


def CreateLead(request):
    context={
        "LeadCreationForm":LeadCreationForm
    }
    return render(request,"leads/leads_create.html",context)
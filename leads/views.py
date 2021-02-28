from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import LeadModel
from .forms import LeadCreationForm
# Create your views here.


def index(request):
    print(request)
    return HttpResponse("Received")

def LeadList(request):
     leads=LeadModel.objects.all()
     context={
         "leads":leads
     }
     return render(request,"leads/leads_list.html",context)


def LeadCreate(request):
    if request.POST:
        form =LeadCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("leadlist")

    context={
        "LeadCreationForm":LeadCreationForm
    }
    return render(request,"leads/leads_create.html",context)


def LeadDetail(request,pk):
    lead=LeadModel.objects.get(id=pk)
    context={
        "lead":lead
    }
    return render(request,"leads/leads_detail.html",context)


def LeadUpdate(request,pk):
    lead=LeadModel.objects.get(id=pk)
    form=LeadCreationForm(instance=lead)
    if request.POST:
        form =LeadCreationForm(request.POST,instance=lead)
        if form.is_valid():
            form.save()
            return redirect("leadlist")
    context={
        #"lead":lead,
        "form":form,
        "lead":lead,
            }
    return render(request,"leads/leads_update.html",context)        
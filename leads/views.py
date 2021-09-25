from django.core.mail import send_mail
from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import AgentModel, LeadModel
from .forms import LeadCreationForm,UserCreationForm
from agents.mixin import OrganisorAndLoginRequiredMixin
from django.views.generic import (
                                    TemplateView,
                                    CreateView,
                                    ListView,
                                    UpdateView,
                                    DeleteView,
                                    DetailView,
                                ) 

class LandingPageView(TemplateView):
    template_name="leads/index.html"


class SignupView(CreateView):
    template_name="registration/signup.html"
    form_class=UserCreationForm

    def get_success_url(self):
        return reverse("login")

def index(request):
    return render(request,"leads/index.html")

class LeadListView(LoginRequiredMixin,ListView):
    template_name="leads/leads_list.html"
    context_object_name="leads"


    def get_queryset(self):
        user=self.request.user

        #queryset of leads for the entire organisation
        if user.is_organisor:
            queryset=LeadModel.objects.filter(organisation=user.userprofile,agent__isnull=False)
        else:
            queryset=LeadModel.objects.filter(organisation = user.agent.organisation)
            #filter for the agent that is logged in
            queryset=queryset.filter(agent__user=user)
        
        return queryset  

    def get_context_data(self,**kwargs):
        context=super(LeadListView,self).get_context_data(**kwargs)
        user=self.request.user
        if user.is_organisor:
            queryset=LeadModel.objects.filter(
                                organisation=user.userprofile,
                                agent__isnull=True,
                            )
            context.update({
                 'unassigned_leads':queryset     
            })   
              

def LeadList(request):
     leads=LeadModel.objects.all()
     context={
         "leads":leads
     }
     return render(request,"leads/leads_list.html",context)


class LeadCreateView(OrganisorAndLoginRequiredMixin,CreateView):
    template_name="leads/leads_create.html"
    form_class=LeadCreationForm

    def get_success_url(self):
        return reverse("leads:leadlist")

    def form_valid(self,form):
        
        lead = form.save(commit=False)
        lead.organisation = self.request.user.userprofile
        lead.save()

        send_mail(
            subject="A lead has been created",
            message="Go to the site to see the new lead",
            from_email="test@test.com",
            recipient_list=['test2@test.com']
            # recipient_list=["test2@test.com"]
        )
        return super(LeadCreateView,self).form_valid(form)

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

class LeadDetailView(LoginRequiredMixin,DetailView):
    template_name="leads/leads_detail.html"

    context_object_name="lead"
    def get_queryset(self):
        user=self.request.user

        #queryset of leads for the entire organisation
        if user.is_organisor:
            queryset=LeadModel.objects.filter(organisation=user.userprofile)
        else:
            queryset=LeadModel.objects.filter(organisation =user.agent.organisation)
            #filter for the agent that is logged in
            queryset=queryset.filte(agent__user=user)
        return queryset    


def LeadDetail(request,pk):
    lead=LeadModel.objects.get(id=pk)
    context={
        "lead":lead
    }
    return render(request,"leads/leads_detail.html",context)


class LeadUpdateView(OrganisorAndLoginRequiredMixin,UpdateView):
    template_name="leads/leads_update.html"
    #queryset=LeadModel.objects.all()
    form_class=LeadCreationForm
    context_object_name="lead"
    def get_queryset(self):
        user=self.request.user
        #queryset of leads for the entire organisation
        queryset=LeadModel.objects.filter(organisation=user.userprofile)
       
        

    def get_success_url(self):
        return reverse("leads:leadlist") 

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

class LeadDeleteView(LoginRequiredMixin,DeleteView):
    template_name="leads/leads_delete.html"

    def get_queryset(self):
        user=self.request.user
        #queryset of leads for the entire organisation
        queryset=LeadModel.objects.filter(organisation=user.userprofile)
       

    def get_success_url(self):
        return reverse("leads:leadlist")    


def LeadDelete(request,pk):
    lead=LeadModel.objects.get(id=pk)
    lead.delete()
    return redirect("leads:leadlist")   
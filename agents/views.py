import random
from django.shortcuts import render,reverse
from django.views.generic import (
                                 ListView,
                                 CreateView,
                                 DetailView,
                                 UpdateView,
                                 DeleteView,
                                 )
from leads.models import AgentModel
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import AgentModelForm
from .mixin import OrganisorAndLoginRequiredMixin
from django.core.mail import send_mail
# Create your views here.

class AgentListView(OrganisorAndLoginRequiredMixin,ListView):
    template_name="agents/agent_list.html"
    context_object_name="agents"

    def get_queryset(self):
        organisation=self.request.user.userprofile
        return AgentModel.objects.filter(organisation=organisation)


class AgentCreatView(OrganisorAndLoginRequiredMixin,CreateView):
    template_name="agents/agent_create.html"
    form_class=AgentModelForm

    def  get_success_url(self):
        return reverse("agents:agents")

    def form_valid(self,form):
        user=form.save(commit=False)
        user.is_agent=True
        user.is_organisor=False
        user.set_password(f"{random.randint(1,100000)}")
        user.save()
        AgentModel.objects.create(
            user=user,
            organisation=self.request.user.userprofile
        )

        send_mail(
            subject="You assigned as agent",
            message="You have been assigned as agent.",
            from_email="admin@test.com",
            recipient_list=['agenttest2@test.com']
        )
        return super(AgentCreatView,self).form_valid(form)


class AgentDetailView(OrganisorAndLoginRequiredMixin,DetailView):
    template_name="agents/agent_detail.html"
    context_object_name="agent"
    queryset=AgentModel.objects.all()

    def get_queryset(self):
        return AgentModel.objects.all()

    
class AgentUpdateView(OrganisorAndLoginRequiredMixin,UpdateView):
    template_name="agents/agent_update.html"
    form_class=AgentModelForm
    context_object_name="agent"

    def  get_success_url(self):
        return reverse("agents:agents")

    def get_queryset(self):
        return AgentModel.objects.all()
    

class AgentDeleteView(OrganisorAndLoginRequiredMixin,DeleteView):
    template_name="agents/agent_delete.html"
    queryset=AgentModel.objects.all()


    def get_success_url(self):
        return reverse("agents:agents")  
    
    

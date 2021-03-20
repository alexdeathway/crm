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
# Create your views here.

class AgentListView(LoginRequiredMixin,ListView):
    template_name="agents/agent_list.html"
    context_object_name="agents"

    def get_queryset(self):
        return AgentModel.objects.all()


class AgentCreatView(LoginRequiredMixin,CreateView):
    template_name="agents/agent_create.html"
    form_class=AgentModelForm

    def  get_success_url(self):
        return reverse("agents:agents")

    def form_valid(self,form):
        agent=form.save(commit=False)
        agent.organisation=self.request.user.userprofile
        agent.save()
        return super(AgentCreatView,self).form_valid(form)


class AgentDetailView(LoginRequiredMixin,DetailView):
    template_name="agents/agent_detail.html"
    context_object_name="agent"
    queryset=AgentModel.objects.all()

    def get_queryset(self):
        return AgentModel.objects.all()

    
class AgentUpdateView(LoginRequiredMixin,UpdateView):
    template_name="agents/agent_update.html"
    form_class=AgentModelForm
    context_object_name="agent"

    def  get_success_url(self):
        return reverse("agents:agents")

    def get_queryset(self):
        return AgentModel.objects.all()
    

class AgentDeleteView(LoginRequiredMixin,DeleteView):
    template_name="agents/agent_delete.html"
    queryset=AgentModel.objects.all()


    def get_success_url(self):
        return reverse("agents:agents")  
    
    

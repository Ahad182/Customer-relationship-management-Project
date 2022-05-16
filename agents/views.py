import random
from django.shortcuts import render,reverse
from django.views import generic
from agents.Mixins import is_orgnaizerAndLoginRequiredMixin
from agents.forms import AgentModelForm

from leads.models import Agent
from django.core.mail import send_mail


# Create your views here.

class AgentListView(is_orgnaizerAndLoginRequiredMixin,generic.ListView):
    template_name = 'agents/agent_list.html'
    context_object_name = 'agents'

    def get_queryset(self):
        orgnaization = self.request.user.userprofile
        return Agent.objects.filter(organization=orgnaization)


class AgentCreateView(is_orgnaizerAndLoginRequiredMixin,generic.CreateView):
    template_name = 'agents/agent_create.html'
    form_class = AgentModelForm
    
    def get_success_url(self):
        return reverse('agents:agent_list')

    def form_valid(self,form):
        user = form.save(commit=False)
        user.is_agent = True
        user.is_orgnaizer = False
        user.set_password(f"{random.randint(0,100000)}")
        user.save()
        Agent.objects.create(user=user, organization=self.request.user.userprofile)

        send_mail(
            subject='Lead has been created',
            message='check your DJCRM Lead',
            from_email = 'lead@gmail.com',
            recipient_list= [user.email],
        )

        return super(AgentCreateView , self).form_valid(form)
    

class AgentUpdateView(is_orgnaizerAndLoginRequiredMixin,generic.UpdateView):
    template_name = 'agents/agent_update.html'
    form_class = AgentModelForm
    context_object_name = 'agent'

    def get_queryset(self):
        orgnaization = self.request.user.userprofile
        return Agent.objects.filter(organization=orgnaization)

    
    def get_success_url(self):
        return reverse('agent_list')

class AgentDetailView(is_orgnaizerAndLoginRequiredMixin,generic.DetailView):
    template_name = 'agents/agent_detail.html'
    context_object_name = 'agent'


    def get_queryset(self):
        orgnaization = self.request.user.userprofile
        return Agent.objects.filter(organization=orgnaization)


class AgentDeleteView(is_orgnaizerAndLoginRequiredMixin,generic.DeleteView):
    template_name = 'agents/agent_delete.html'
    def get_queryset(self):
        orgnaization = self.request.user.userprofile
        return Agent.objects.filter(organization=orgnaization)


    def get_success_url(self):
        return reverse('agent_list')

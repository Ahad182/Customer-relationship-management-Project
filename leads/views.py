from django.shortcuts import redirect, render,reverse
from leads.forms import CategoryForm, CostumUserCreationForm, LeadModelForm
from django.views.generic import (
    TemplateView,
    ListView,
    DetailView,
    CreateView,UpdateView,
    DeleteView
    )

from leads.models import Category, Lead
from django.core.mail import send_mail
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class SignupView(CreateView):
    template_name = 'registration/signup.html'
    form_class = CostumUserCreationForm

    
    def get_success_url(self):
        return reverse('login')


class LandingPageView(TemplateView):
    template_name = 'pages/home.html'


# def home(request):
#     return render(request, 'pages/home.html')


class LeadListView(LoginRequiredMixin,ListView):
    template_name = 'leads/lead_list.html'
    context_object_name = 'leads'

    def get_queryset(self):
        user = self.request.user
        if user.is_orgnaizer:
            queryset = Lead.objects.filter(organization=user.userprofile, agent__isnull=False)
        else :
            queryset = Lead.objects.filter(organization=user.agent.organization)
            queryset = queryset.filter(agent__user=self.request.user)
        return queryset


    def get_context_data(self, **kwargs):
        context = super(LeadListView,self).get_context_data(**kwargs)
        user = self.request.user
        if user.is_orgnaizer:
            queryset = Lead.objects.filter(organization=user.userprofile , agent__isnull=True)
            context.update({
                'Unassignes_leads':queryset,
            })
            return context

# def lead_list(request):
#     leads = Lead.objects.all()

#     context = {
#         'leads':leads,
#     }
#     return render(request, 'leads/lead_list.html',context)

class LeadDetailView(LoginRequiredMixin,DetailView):
    template_name = 'leads/lead_detail.html'
    context_object_name = 'lead'

    def get_queryset(self):
        user = self.request.user
        if user.is_orgnaizer:
            queryset = Lead.objects.filter(organization=user.userprofile)
        else :
            queryset = Lead.objects.filter(organization=user.agent.organization)
            queryset = queryset.filter(agent__user=self.request.user)
        return queryset

# def lead_detail(request,pk):
#     lead = Lead.objects.get(pk=pk)
#     context = {
#         'lead':lead,
#     }

#     return render(request, 'leads/lead_detail.html', context)


class LeadCreateView(LoginRequiredMixin,CreateView):
    template_name = 'leads/lead_create.html'
    form_class = LeadModelForm
    def get_success_url(self):
        return reverse('lead_list')
    
    def form_valid(self, form):
        send_mail(
            subject='Lead has been created',
            message='check your DJCRM Lead',
            from_email = 'lead@gmail.com',
            recipient_list= ['Newlead@gmail.com'],
        )
        return super(LeadCreateView,self).form_valid(form)


# def lead_create(request):
#     form = LeadModelForm()
#     if request.method == 'POST':
#         form = LeadModelForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('lead_list')
#     context = {'form':form}
#     return render(request, 'leads/lead_create.html', context)
class LeadUpdateView(LoginRequiredMixin,UpdateView):
    template_name = 'leads/lead_update.html'
    form_class = LeadModelForm
    def get_success_url(self):
        return reverse('lead_list')

    def get_queryset(self):
        user = self.request.user
        if user.is_orgnaizer:
            return Lead.objects.filter(organization=user.userprofile)
       
# def lead_update(request,pk):
#     lead = Lead.objects.get(pk=pk)
#     form = LeadModelForm(instance=lead)
#     if request.method == 'POST':
#         form = LeadModelForm(request.POST,instance=lead)
#         if form.is_valid():
#             form.save()
#             return redirect('lead_list')

#     context = {
#         'form':form,
#         'lead':lead
#         }
#     return render(request, 'leads/lead_update.html', context)

class LeadsDeleteView(LoginRequiredMixin,DeleteView):
    template_name = 'leads/lead_delete.html'
    
    def get_queryset(self):
        user = self.request.user
        if user.is_orgnaizer:
            return Lead.objects.filter(organization=user.userprofile)


# def lead_delete(request,pk):
#     lead = Lead.objects.get(pk=pk)
#     lead.delete()
#     return redirect('lead_list')




class CategoryListView(LoginRequiredMixin,ListView):
    template_name = 'category/category_list.html'
    context_object_name= 'category_list'

    def get_queryset(self):
        user = self.request.user
        if user.is_orgnaizer:
            queryset = Category.objects.filter(organization=user.userprofile)
        else:
            queryset = Category.objects.filter(organization=user.agent.organization)
        return queryset


    def get_context_data(self, **kwargs):
        context = super(CategoryListView, self).get_context_data(**kwargs)
        user = self.request.user
        if user.is_orgnaizer:
            queryset = Lead.objects.filter(organization=user.userprofile , category__isnull=True).count()
            context.update({
                'unassigned_category_count':queryset,
            })
            return context


class CategoryDetailView(LoginRequiredMixin,DetailView):
    template_name = 'category/category_detail.html'
    context_object_name = 'category'

    def get_queryset(self):
        user = self.request.user
        if user.is_orgnaizer:
            queryset = Category.objects.filter(organization=user.userprofile)
        else:
            queryset = Category.objects.filter(organization=user.agent.organization)
        return queryset


class CategoryUpdateView(LoginRequiredMixin,UpdateView):
    template_name = 'category/category_update.html'
    form_class = CategoryForm

    def get_queryset(self):
        user = self.request.user
        if user.is_orgnaizer:
            queryset = Lead.objects.filter(organization=user.userprofile)
        else :
            queryset = Lead.objects.filter(organization=user.agent.organization)
            queryset = queryset.filter(agent__user=self.request.user)
        return queryset

    def get_success_url(self):
        return reverse('lead_detail',kwargs={'pk': self.get_object().id})

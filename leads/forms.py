from django import forms
from leads.models import Lead
from django.contrib.auth.forms import UserCreationForm,UsernameField
from django.contrib.auth import get_user_model


User = get_user_model()

class LeadModelForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = '__all__'



class CostumUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username',)
        field_classes = {'username': UsernameField }



class CategoryForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = (
            'category',
        )
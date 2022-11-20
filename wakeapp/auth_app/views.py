from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as generic_views
from wakeapp.auth_app import forms


class UserRegistrationView(generic_views.CreateView):
    template_name = 'account/profile_register.html'
    form_class = forms.CreateUserForm
    success_url = reverse_lazy('dashboard')


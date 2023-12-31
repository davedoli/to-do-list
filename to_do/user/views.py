from django.shortcuts import render

# Create your views here.
from django.views import generic
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm
from django.contrib.auth import get_user_model
User = get_user_model()

class SignUpView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"
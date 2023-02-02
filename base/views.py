from django.shortcuts import render, reverse
from django.views import generic
from django.contrib.auth.forms import UserCreationForm

class LandingPageView(generic.TemplateView):
    template_name = "landing.html"

class SignupView(generic.CreateView):
    template_name = 'registration/signup.html'
    form_class = UserCreationForm

    def get_success_url(self) -> str:
        return reverse('login')






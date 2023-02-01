from django.shortcuts import render
from django.views import generic

class LandingPageView(generic.TemplateView):
    template_name = "landing.html"






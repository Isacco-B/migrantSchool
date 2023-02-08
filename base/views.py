from django.shortcuts import render, reverse
from django.views import generic
from .forms import StudentForm
from .models import Certificate

class LandingPageView(generic.TemplateView):
    template_name = "landing.html"


class SignupView(generic.CreateView):
    template_name = 'registration/signup.html'
    form_class = StudentForm

    def get_success_url(self) -> str:
        return reverse('login')

class SearchResultsView(generic.ListView):
    model = Certificate
    template_name = 'search_result.html'
    context_object_name = 'certificates'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Certificate.objects.filter(transaction_id__icontains=query)
        return object_list













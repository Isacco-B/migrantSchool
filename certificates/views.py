from django.shortcuts import render, reverse
from django.views import generic
from base.models import Certificate
from base.forms import CertificateForm


class CertificateListView(generic.ListView):
    template_name = 'certificates/certificate_list.html'
    context_object_name = 'certificates'

    def get_queryset(self):
        return Certificate.objects.all()


class CertificateCreateView(generic.CreateView):
    template_name = 'certificates/certificate_create.html'
    form_class = CertificateForm

    def get_success_url(self) -> str:
        return reverse('certificates:certificate-list')

class CertificateDetailView(generic.DeleteView):
    template_name = 'certificates/certificate_detail.html'
    context_object_name = 'certificates'

    def get_queryset(self):
        return Certificate.objects.all()


class CertificateUpdateView(generic.UpdateView):
    template_name = 'certificates/certificate_update.html'
    context_object_name = 'certificates'
    queryset = Certificate.objects.all()
    form_class = CertificateForm

    def get_success_url(self) -> str:
        return reverse('certificates:certificate-list')

    def get_queryset(self):
        return Certificate.objects.all()


class CertificateDeleteView(generic.DeleteView):
    pass

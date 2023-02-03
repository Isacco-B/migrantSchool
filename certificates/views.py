from django.shortcuts import render, reverse
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from base.models import Certificate
from base.forms import CertificateForm
from .mixins import StaffAndLoginRequiredMixin


class CertificateListView(generic.ListView):
    template_name = 'certificates/certificate_list.html'
    context_object_name = 'certificates'

    def get_queryset(self):
        if self.request.user.is_staff:
            return Certificate.objects.all()
        elif self.request.user.is_authenticated:
            return Certificate.objects.filter(student=self.request.user.pk)
        else:
            return Certificate.objects.all()



class CertificateCreateView(StaffAndLoginRequiredMixin, generic.CreateView):
    template_name = 'certificates/certificate_create.html'
    form_class = CertificateForm

    def get_success_url(self) -> str:
        return reverse('certificates:certificate-list')


class CertificateDetailView(generic.DeleteView):
    template_name = 'certificates/certificate_detail.html'
    context_object_name = 'certificates'

    def get_queryset(self):
        return Certificate.objects.all()


class CertificateUpdateView(StaffAndLoginRequiredMixin, generic.UpdateView):
    template_name = 'certificates/certificate_update.html'
    context_object_name = 'certificates'
    form_class = CertificateForm

    def get_success_url(self) -> str:
        return reverse('certificates:certificate-list')

    def get_queryset(self):
        return Certificate.objects.all()


class CertificateDeleteView(StaffAndLoginRequiredMixin, generic.DeleteView):
    template_name = 'certificates/certificate_delete.html'
    context_object_name = 'certificates'

    def get_queryset(self):
        return Certificate.objects.all()

    def get_success_url(self) -> str:
        return reverse('certificates:certificate-list')

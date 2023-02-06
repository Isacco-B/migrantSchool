from django.shortcuts import render, reverse
from django.contrib import messages
from django.views import generic
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from base.models import Certificate
from base.forms import CertificateForm
from base.utils import sendTransaction, get_transaction
from .mixins import StaffAndLoginRequiredMixin


class CertificateListView(LoginRequiredMixin, generic.ListView):
    template_name = 'certificates/certificate_list.html'
    context_object_name = 'certificates'

    def get_queryset(self):
        if self.request.user.is_staff:
            return Certificate.objects.all()
        elif self.request.user.is_authenticated:
            return Certificate.objects.filter(student=self.request.user.pk)


class CertificateCreateView(StaffAndLoginRequiredMixin, generic.CreateView):
    template_name = 'certificates/certificate_create.html'
    form_class = CertificateForm

    def get_success_url(self) -> str:
        return reverse('certificates:certificate-list')

    def form_valid(self, form):
        messages.success(self.request, 'You have successfuly created a certificate')
        return super(CertificateCreateView, self).form_valid(form)


class CertificateDetailView(generic.DetailView):
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

    def form_valid(self, form):
        form.save()
        messages.info(self.request, 'You have successfuly update a certificate')
        return super(CertificateUpdateView, self).form_valid(form)


class CertificateDeleteView(StaffAndLoginRequiredMixin, generic.DeleteView):
    template_name = 'certificates/certificate_delete.html'
    context_object_name = 'certificates'

    def get_queryset(self):
        return Certificate.objects.all()

    def get_success_url(self) -> str:
        return reverse('certificates:certificate-list')


def TransactionDetailView(request):
    transiction = get_transaction('0xdf9ab500a87d92d058c65053ce831d648052d82fdacd8f6aac5a945c12d72832')
    context = {
        "transiction": transiction
    }
    return render(request, "certificates/transaction_detail.html", context)



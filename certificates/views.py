from django.shortcuts import render
from django.views import generic


class CertificateListView(generic.ListView):
    template_name = 'certificats/certificate_list.html'
    context_object_name = 'certificates'

    def get_queryset(self):
        pass


class CertificateCreateView(generic.CreateView):
    pass


class CertificateDetailView(generic.DeleteView):
    pass


class CertificateUpdateView(generic.UpdateView):
    pass


class CertificateDeleteView(generic.DeleteView):
    pass

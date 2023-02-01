from django.shortcuts import render
from django.views import generic


class StudentListView(generic.ListView):
    pass


class StudentCreateView(generic.CreateView):
    pass


class StudentDetailView(generic.DeleteView):
    pass


class StudentUpdateView(generic.UpdateView):
    pass


class StudentDeleteView(generic.DeleteView):
    pass


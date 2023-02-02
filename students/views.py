from django.shortcuts import render, reverse
from django.views import generic
from base.models import User
from base.forms import StudentForm, StudentUpdateForm


class StudentListView(generic.ListView):
    template_name = 'students/student_list.html'
    context_object_name = 'students'

    def get_queryset(self):
        return User.objects.all()


class StudentCreateView(generic.CreateView):
    template_name = 'students/student_create.html'
    context_object_name = 'students'
    queryset = User.objects.all()
    form_class = StudentForm

    def get_success_url(self) -> str:
        return reverse('students:student-list')

    def get_queryset(self):
        return User.objects.all()


class StudentDetailView(generic.DetailView):
    template_name = 'students/student_detail.html'
    context_object_name = 'students'

    def get_queryset(self):
        return User.objects.all()


class StudentUpdateView(generic.UpdateView):
    template_name = 'students/student_update.html'
    context_object_name = 'students'
    queryset = User.objects.all()
    form_class = StudentUpdateForm

    def get_queryset(self):
        return User.objects.all()

    def get_success_url(self) -> str:
        return reverse('students:student-list')



class StudentDeleteView(generic.DeleteView):
    template_name = 'students/student_delete.html'
    context_object_name = 'students'

    def get_queryset(self):
        return User.objects.all()

    def get_success_url(self) -> str:
        return reverse('students:student-list')

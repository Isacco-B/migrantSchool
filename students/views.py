from django.shortcuts import render, reverse
from django.contrib import messages
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from base.models import User
from base.forms import StudentForm, StudentUpdateForm




class StudentListView(LoginRequiredMixin, generic.ListView):
    template_name = 'students/student_list.html'
    context_object_name = 'students'

    def get_queryset(self):
        if self.request.user.is_staff:
            return User.objects.all()
        else:
            return User.objects.filter(pk=self.request.user.pk)


class StudentCreateView(LoginRequiredMixin, generic.CreateView):
    template_name = 'students/student_create.html'
    context_object_name = 'students'
    form_class = StudentForm

    def get_success_url(self) -> str:
        return reverse('students:student-list')

    def get_queryset(self):
        return User.objects.all()

    def form_valid(self, form):
        messages.success(self.request, 'You have successfuly created a student')
        return super(StudentCreateView, self).form_valid(form)


class StudentDetailView(LoginRequiredMixin, generic.DetailView):
    template_name = 'students/student_detail.html'
    context_object_name = 'students'

    def get_queryset(self):
        return User.objects.all()


class StudentUpdateView(LoginRequiredMixin, generic.UpdateView):
    template_name = 'students/student_update.html'
    context_object_name = 'students'
    form_class = StudentUpdateForm

    def get_queryset(self):
        return User.objects.all()

    def get_success_url(self) -> str:
        return reverse('students:student-list')

    def form_valid(self, form):
        form.save()
        messages.info(self.request, 'You have successfuly update a student')
        return super(StudentUpdateView, self).form_valid(form)



class StudentDeleteView(LoginRequiredMixin, generic.DeleteView):
    template_name = 'students/student_delete.html'
    context_object_name = 'students'

    def get_queryset(self):
        return User.objects.all()

    def get_success_url(self) -> str:
        return reverse('students:student-list')

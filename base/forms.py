from django import forms
from django.contrib.auth.forms import UserCreationForm, UsernameField
from base.models import Certificate, User

class CertificateForm(forms.ModelForm):

    class Meta:
        model = Certificate
        fields = '__all__'


class StudentForm(UserCreationForm):

    class Meta:
        model = User
        fields = (
            "username",
            'first_name',
            'last_name',
            'age',
            'gender',
            'email',
            'address',
            'phone_number',
            )
        field_classes = {"username": UsernameField}

class StudentUpdateForm(forms.ModelForm):

    class Meta:
        model = User
        fields =  (
            'username',
            'first_name',
            'last_name',
            'email',
            'age',
            'address',
            'phone_number',
        )

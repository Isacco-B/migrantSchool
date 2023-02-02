from django import forms
from base.models import Certificate, User

class CertificateForm(forms.ModelForm):

    class Meta:
        model = Certificate
        fields = '__all__'


class StudentForm(forms.ModelForm):

    class Meta:
        model = User
        fields =  (
            'username',
            'first_name',
            'last_name',
            'email',
            'password',
            'age',
            'gender',
            'address',
            'phone_number',
        )

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

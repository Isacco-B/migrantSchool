from django import forms
from base.models import Certificate

class CertificateForm(forms.ModelForm):

    class Meta:
        model = Certificate
        fields = '__all__'


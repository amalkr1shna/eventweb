from django import forms
from .models import Applicant
class ApplicantForm(forms.ModelForm):
    class Meta:
        model=Applicant
        fields=ApplicantFormfields=['full_name','email','phone']
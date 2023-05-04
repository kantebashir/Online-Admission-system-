from django import forms
from django.forms import ModelForm
from django.forms.models import inlineformset_factory #formset is all about layer of abstraction to work with multiple forms on the same page
from django.contrib.auth import get_user_model
from models.applicant_model import ApplicantProfile,ApplicantPrevEducation


class DateInput(forms.DateInput):
    input_type = 'date'

class ApplicantProfileForm(ModelForm):

    class Meta:
        model = ApplicantProfile
        exclude = ('owner',)
        widgets = {
            'DOB': DateInput(),
        }



class ApplicantPrevEducationForm(ModelForm):
    class Meta:
        model = ApplicantPrevEducation
        fields = '__all__'



ApplicantPrevEducationFormSet = inlineformset_factory(ApplicantProfile, ApplicantPrevEducation, form=ApplicantPrevEducationForm, extra=1)
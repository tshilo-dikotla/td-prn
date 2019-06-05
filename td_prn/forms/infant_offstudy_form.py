from django import forms
from edc_form_validators import FormValidator

from ..form_validators import OffstudyFormValidator
from ..models import InfantOffStudy


class InfantOffStudyForm(OffstudyFormValidator, FormValidator, forms.ModelForm):

    class Meta:
        model = InfantOffStudy
        fields = '__all__'

from django import forms
from edc_form_validators import FormValidator

from ..form_validators import OffstudyFormValidator
from ..models import MaternalOffStudy


class MaternalOffStudyForm(OffstudyFormValidator, FormValidator, forms.ModelForm):

    class Meta:
        model = MaternalOffStudy
        fields = '__all__'

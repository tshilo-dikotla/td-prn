from django import forms

from ..form_validators import OffstudyFormValidator
from ..models import InfantOffStudy


class InfantOffStudyForm(forms.ModelForm):

    form_validator_cls = OffstudyFormValidator

    class Meta:
        model = InfantOffStudy
        fields = '__all__'

from django import forms
from ..form_validators import OffstudyFormValidator
from ..models import MaternalOffStudy


class MaternalOffStudyForm(forms.ModelForm):

    form_validator_cls = OffstudyFormValidator

    class Meta:
        model = MaternalOffStudy
        fields = '__all__'

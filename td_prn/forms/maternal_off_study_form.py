from django import forms
from edc_form_validators import FormValidatorMixin

from ..form_validators import OffstudyFormValidator
from ..models import MaternalOffStudy


class MaternalOffStudyForm(FormValidatorMixin, forms.ModelForm):

    form_validator_cls = OffstudyFormValidator

    def clean(self):
        super().clean()
        print(self.cleaned_data)

    class Meta:
        model = MaternalOffStudy
        fields = '__all__'

from django import forms
from edc_form_validators import FormValidatorMixin

from ..form_validators import OffstudyFormValidator
from ..models import MaternalOffStudy


class MaternalOffStudyForm(FormValidatorMixin, forms.ModelForm):

    form_validator_cls = OffstudyFormValidator

    def clean(self):
        super().clean()
        self.validate_against_consent_datetime(
            self.cleaned_data.get('report_datetime'))

    class Meta:
        model = MaternalOffStudy
        fields = '__all__'

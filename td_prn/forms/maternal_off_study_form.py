
from django import forms
from edc_form_validators import FormValidatorMixin
from td_maternal_validators.form_validators.form_validator_mixin import (
    TDFormValidatorMixin)

from ..form_validators import OffstudyFormValidator
from ..models import MaternalOffStudy


class MaternalOffStudyForm(FormValidatorMixin, TDFormValidatorMixin,
                           forms.ModelForm):

    OffstudyFormValidator.visit_model = 'td_maternal.maternalvisit'

    form_validator_cls = OffstudyFormValidator

    def clean(self):
        self.subject_identifier = self.cleaned_data.get('subject_identifier')

        super().clean()
        self.validate_against_consent_datetime(
            self.cleaned_data.get('report_datetime'))

    class Meta:
        model = MaternalOffStudy
        fields = '__all__'

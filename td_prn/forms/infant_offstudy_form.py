from django import forms
from edc_form_validators import FormValidatorMixin

from td_infant_validators.form_validators import InfantFormValidatorMixin

from ..form_validators import OffstudyFormValidator
from ..models import InfantOffStudy


class InfantOffStudyForm(InfantFormValidatorMixin, FormValidatorMixin,
                         forms.ModelForm):

    form_validator_cls = OffstudyFormValidator

    def clean(self):
        super().clean()

        self.validate_against_birth_date(
            infant_identifier=self.subject_identifier,
            report_datetime=self.cleaned_data.get('report_datetime'))

    class Meta:
        model = InfantOffStudy
        fields = '__all__'

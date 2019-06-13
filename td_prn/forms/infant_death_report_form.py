from django import forms

from ..form_validators import DeathReportFormValidator
from ..models import InfantDeathReport


class InfantDeathReportForm(forms.ModelForm):

    form_validator_cls = DeathReportFormValidator

    def clean(self):
        self.subject_identifier = self.cleaned_data.get(
            'subject_identifier')
        self.validate_against_birth_date(
            infant_identifier=self.subject_identifier,
            report_datetime=self.cleaned_data.get('report_datetime'))
        super().clean()

    class Meta:
        model = InfantDeathReport
        fields = '__all__'

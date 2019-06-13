from django import forms

from ..form_validators import DeathReportFormValidator
from ..models import MaternalDeathReport


class MaternalDeathReportForm(forms.ModelForm):

    form_validator_cls = DeathReportFormValidator

    def clean(self):
        self.subject_identifier = self.cleaned_data.get(
            'subject_identifier')
        self.validate_against_consent_datetime(
            self.cleaned_data.get('report_datetime'))
        super().clean()

    class Meta:
        model = MaternalDeathReport
        fields = '__all__'

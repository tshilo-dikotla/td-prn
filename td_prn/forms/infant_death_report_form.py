from django import forms

from ..form_validators import DeathReportFormValidator
from ..models import InfantDeathReport


class InfantDeathReportForm(forms.ModelForm):

    form_validator_cls = DeathReportFormValidator

    class Meta:
        model = InfantDeathReport
        fields = '__all__'

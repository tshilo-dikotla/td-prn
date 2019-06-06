from django import forms

from ..form_validators import DeathReportFormValidator
from ..models import MaternalDeathReport


class MaternalDeathReportForm(forms.ModelForm):

    form_validator_cls = DeathReportFormValidator

    class Meta:
        model = MaternalDeathReport
        fields = '__all__'

from django import forms
from edc_form_validators import FormValidator

from ..form_validators import DeathReportFormValidator
from ..models import MaternalDeathReport


class MaternalDeathReportForm(DeathReportFormValidator, FormValidator, forms.ModelForm):

    class Meta:
        model = MaternalDeathReport
        fields = '__all__'

from django import forms
from edc_form_validators import FormValidator

from ..form_validators import DeathReportFormValidator
from ..models import InfantDeathReport


class InfantDeathReportForm(DeathReportFormValidator, FormValidator, forms.ModelForm):

    class Meta:
        model = InfantDeathReport
        fields = '__all__'

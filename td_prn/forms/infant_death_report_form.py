from django import forms
from ..models import InfantDeathReport


class InfantDeathReportForm(forms.ModelForm):

    class Meta:
        model = InfantDeathReport
        fields = '__all__'

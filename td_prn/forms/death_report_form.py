from django import forms
from ..models import MaternalDeathReport


class DeathReportForm(forms.ModelForm):

    class Meta:
        model = MaternalDeathReport
        fields = '__all__'

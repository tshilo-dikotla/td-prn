from django import forms

from ..models import InfantOffStudy


class InfantOffStudyForm(forms.ModelForm):

    class Meta:
        model = InfantOffStudy
        fields = '__all__'

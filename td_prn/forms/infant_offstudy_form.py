from td_infant_validators.form_validators import InfantFormValidatorMixin

from django import forms

from ..form_validators import OffstudyFormValidator
from ..models import InfantOffStudy


class InfantOffStudyForm(InfantFormValidatorMixin, forms.ModelForm):

    form_validator_cls = OffstudyFormValidator

    def clean(self):
        self.subject_identifier = self.cleaned_data.get(
            'subject_identifier')
        self.validate_against_visit_datetime(
            self.cleaned_data.get('report_datetime'))
        super().clean()

    class Meta:
        model = InfantOffStudy
        fields = '__all__'

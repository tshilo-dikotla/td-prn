from django import forms
from django.core.exceptions import ValidationError
from edc_form_validators import FormValidatorMixin

from td_infant_validators.form_validators import InfantFormValidatorMixin

from ..form_validators import OffstudyFormValidator
from ..models import InfantOffStudy


class InfantOffStudyForm(FormValidatorMixin, InfantFormValidatorMixin,
                         forms.ModelForm):

    OffstudyFormValidator.visit_model = 'td_infant.infantvisit'

    form_validator_cls = OffstudyFormValidator

    def clean(self):
        self.infant_identifier = self.cleaned_data.get('subject_identifier')
        super().clean()

        self.validate_against_birth_date(
            infant_identifier=self.infant_identifier,
            report_datetime=self.cleaned_data.get('report_datetime'))

        self.validate_offstudy_date()

    def validate_offstudy_date(self):
        offstudy_date = self.cleaned_data.get('offstudy_date')
        try:
            infant_birth = self.infant_birth_cls.objects.get(
                subject_identifier=self.infant_identifier)
        except self.infant_birth_cls.DoesNotExist:
            raise ValidationError(
                'Please complete Infant Birth form '
                f'before  proceeding.')
        else:
            if offstudy_date and offstudy_date < infant_birth.report_datetime.date():
                raise forms.ValidationError(
                    "Offstudy date cannot be before enrollemt datetime.")
            else:
                return infant_birth

    class Meta:
        model = InfantOffStudy
        fields = '__all__'

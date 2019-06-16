from django import forms
from django.apps import apps as django_apps
from edc_form_validators import FormValidatorMixin

from td_infant_validators.form_validators import InfantFormValidatorMixin

from ..form_validators import OffstudyFormValidator
from ..models import InfantOffStudy


class InfantOffStudyForm(InfantFormValidatorMixin, FormValidatorMixin,
                         forms.ModelForm):

    form_validator_cls = OffstudyFormValidator

    infant_visit = 'td_maternal.infantvisit'

    @property
    def infant_visit_cls(self):
        return django_apps.get_model(self.infant_visit)

    def clean(self):
        self.infant_identifier = self.cleaned_data.get('subject_identifier')
        self.subject_identifier = self.infant_identifier[:-3]

        super().clean()

        self.validate_against_birth_date(
            infant_identifier=self.infant_identifier,
            report_datetime=self.cleaned_data.get('report_datetime'))

        self.validate_against_birth_date(
            infant_identifier=self.infant_identifier,
            report_datetime=self.cleaned_data.get('offstudy_date'))

        self.validate_against_latest_infant_visit()

    def validate_against_latest_infant_visit(self):
        try:
            infant_visit = self.infant_visit_cls.objects.all().order_by(
                '-report_datetime').first()
            self.previous_visit = infant_visit.report_datetime
        except Exception:
            pass
        else:
            report_datetime = self.cleaned_data.get('report_datetime')
            offstudy_date = self.cleaned_data.get('offstudy_date')
            if report_datetime < self.previous_visit:
                raise forms.ValidationError({
                    'report_datetime': 'Report datetime cannot be '
                    f'before previous visit Got {report_datetime.date()} '
                    f'but previous visit is {self.previous_visit.date()}'
                })
            if offstudy_date and \
                    offstudy_date < self.previous_visit.date():
                raise forms.ValidationError({
                    'offstudy_date': 'Offstudy date cannot be '
                    f'before previous visit Got {offstudy_date} '
                    f'but previous visit is {self.previous_visit.date()}'
                })

    class Meta:
        model = InfantOffStudy
        fields = '__all__'

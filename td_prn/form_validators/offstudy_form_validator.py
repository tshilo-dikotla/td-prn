from django.apps import apps as django_apps
from django.forms import forms
from edc_form_validators import FormValidator
from td_maternal_validators.form_validators.form_validator_mixin import (
    TDFormValidatorMixin)


class OffstudyFormValidator(TDFormValidatorMixin, FormValidator):

    maternal_visit = 'td_maternal.maternalvisit'

    def clean(self):
        super().clean()
        self.subject_identifier = self.cleaned_data.get('subject_identifier')

        self.validate_other_specify(
            field='reason',
            other_specify_field='reason_other',
        )
        self.validate_against_consent_datetime(
            self.cleaned_data.get('report_datetime'))
        self.validate_against_latest_visit()

    @property
    def maternal_visit_cls(self):
        return django_apps.get_model(self.maternal_visit)

    def validate_against_latest_visit(self):
        try:
            maternal_visit = self.maternal_visit_cls.objects.all(
                ).order_by('-report_datetime').first()
            self.previous_visit = maternal_visit.report_datetime
            print('***** previous visit ***** ', self.previous_visit)
        except Exception:
            pass
        else:
            report_datetime = self.cleaned_data.get('report_datetime')
            offstudy_date = self.cleaned_data.get('offstudy_date')
            if report_datetime < maternal_visit.report_datetime:
                raise forms.ValidationError({
                    'report_datetime': 'Report datetime cannot be '
                    f'before previous visit Got {report_datetime.date()} '
                    f'but previous visit is {self.previous_visit.date()}'
                    })
            if offstudy_date and \
                    offstudy_date < maternal_visit.report_datetime.date():
                raise forms.ValidationError({
                    'offstudy_date': 'Offstudy date cannot be '
                    f'before previous visit Got {offstudy_date} '
                    f'but previous visit is {self.previous_visit.date()}'
                    })

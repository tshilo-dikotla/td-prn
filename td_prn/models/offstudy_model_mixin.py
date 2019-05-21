from django.apps import apps as django_apps
from django.core.exceptions import ValidationError
from django.db import models
from edc_base.model_validators import date_not_future
from edc_base.model_validators.date import datetime_not_future
from edc_base.utils import get_utcnow
from edc_protocol.validators import date_not_before_study_start
from edc_protocol.validators import datetime_not_before_study_start

from edc_base.model_fields.custom_fields import OtherCharField


class OffStudyModelMixin:

    report_datetime = models.DateTimeField(
        verbose_name="Report Date",
        validators=[
            datetime_not_before_study_start,
            datetime_not_future],
        default=get_utcnow,
        help_text=('If reporting today, use today\'s date/time, otherwise use'
                   ' the date/time this information was reported.'))

    offstudy_date = models.DateField(
        verbose_name="Off-study Date",
        validators=[
            date_not_before_study_start,
            date_not_future])

    reason_other = OtherCharField()

    comment = models.TextField(
        max_length=250,
        verbose_name="Comment",
        blank=True,
        null=True)

    def get_consent_version(self):
        subject_screening_cls = django_apps.get_model(
            'td_maternal.subjectscreening')
        consent_version_cls = django_apps.get_model(
            'td_maternal.tdconsentversion')
        try:
            subject_screening_obj = subject_screening_cls.objects.get(
                subject_identifier=self.subject_identifier)
        except subject_screening_cls.DoesNotExist:
            raise ValidationError(
                'Missing Subject Screening form. Please complete '
                'it before proceeding.')
        else:
            try:
                consent_version_obj = consent_version_cls.objects.get(
                    screening_identifier=subject_screening_obj.screening_identifier)
            except consent_version_cls.DoesNotExist:
                raise ValidationError(
                    'Missing Consent Version form. Please complete '
                    'it before proceeding.')
            return consent_version_obj.version

    def save(self, *args, **kwargs):
        self.consent_version = self.get_consent_version()
        super(OffStudyModelMixin, self).save(*args, **kwargs)

    class Meta:
        abstract = True

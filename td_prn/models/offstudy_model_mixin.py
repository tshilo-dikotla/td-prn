from django.apps import apps as django_apps
from django.core.exceptions import ValidationError
from django.db import models
from edc_base.model_fields.custom_fields import OtherCharField
from edc_base.model_validators import date_not_future
from edc_protocol.validators import date_not_before_study_start


class OffStudyModelMixin(models.Model):

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

    @property
    def subject_screening_cls(self):
        return django_apps.get_model('td_maternal.subjectscreening')

    @property
    def consent_version_cls(self):
        return django_apps.get_model('td_maternal.tdconsentversion')

    def get_consent_version(self):
        try:
            subject_screening_obj = self.subject_screening_cls.objects.get(
                subject_identifier=self.subject_identifier)
        except self.subject_screening_cls.DoesNotExist:
            raise ValidationError(
                'Missing Subject Screening form. Please complete '
                'it before proceeding.')
        else:
            try:
                consent_version_obj = self.consent_version_cls.objects.get(
                    screening_identifier=subject_screening_obj.screening_identifier)
            except self.consent_version_cls.DoesNotExist:
                raise ValidationError(
                    'Missing Consent Version form. Please complete '
                    'it before proceeding.')
            return consent_version_obj.version

    def save(self, *args, **kwargs):
        self.consent_version = self.get_consent_version()
        super(OffStudyModelMixin, self).save(*args, **kwargs)

    class Meta:
        abstract = True

from django.apps import apps as django_apps
from django.core.exceptions import ValidationError
from django.db import models
from edc_base.model_managers import HistoricalRecords
from edc_base.model_mixins import BaseUuidModel
from edc_base.model_validators.date import datetime_not_future
from edc_base.utils import get_utcnow
from edc_identifier.managers import SubjectIdentifierManager
from edc_identifier.model_mixins import TrackingIdentifierModelMixin
from edc_protocol.validators import datetime_not_before_study_start
from edc_visit_schedule.model_mixins import OffScheduleModelMixin
from edc_visit_schedule.site_visit_schedules import site_visit_schedules

from edc_action_item.model_mixins.action_model_mixin import ActionModelMixin

from ..action_items import INFANTOFF_STUDY_ACTION
from ..choices import INFANT_OFF_STUDY_REASON
from .offstudy_model_mixin import OffStudyModelMixin


class InfantOffStudy(OffStudyModelMixin, OffScheduleModelMixin,
                     ActionModelMixin, BaseUuidModel):

    """ A model completed by the user when the infant is taken off study. """

    tracking_identifier_prefix = 'IO'

    action_name = INFANTOFF_STUDY_ACTION

    report_datetime = models.DateTimeField(
        verbose_name="Report Date",
        validators=[
            datetime_not_before_study_start,
            datetime_not_future],
        default=get_utcnow,
        help_text=('If reporting today, use today\'s date/time, otherwise use'
                   ' the date/time this information was reported.'))

    reason = models.CharField(
        verbose_name=('Please code the primary reason participant taken'
                      ' off-study'),
        max_length=115,
        choices=INFANT_OFF_STUDY_REASON)

    objects = SubjectIdentifierManager()

    history = HistoricalRecords()

    def take_off_schedule(self):
        infant_schedule_model = django_apps.get_model(
            'td_infant.onscheduleinfantbirth')

        try:
            on_schedule_obj = infant_schedule_model.objects.get(
                subject_identifier=self.subject_identifier)
        except infant_schedule_model.DoesNotExist:
            pass
        else:
            _, schedule = \
                site_visit_schedules.get_by_onschedule_model_schedule_name(
                    onschedule_model='td_infant.onscheduleinfantbirth',
                    name=on_schedule_obj.schedule_name)
            schedule.take_off_schedule(offschedule_model_obj=self)

    def get_consent_version(self):
        subject_screening_cls = django_apps.get_model(
            'td_maternal.subjectscreening')
        consent_version_cls = django_apps.get_model(
            'td_maternal.tdconsentversion')
        try:
            subject_screening_obj = subject_screening_cls.objects.get(
                subject_identifier=self.subject_identifier[:-3])
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

    class Meta:
        app_label = 'td_prn'
        verbose_name = "Infant Off-Study"
        verbose_name_plural = "Infant Off-Study"

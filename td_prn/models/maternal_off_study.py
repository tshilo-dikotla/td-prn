from django.apps import apps as django_apps
from django.db import models
from edc_base.model_managers import HistoricalRecords
from edc_base.model_mixins import BaseUuidModel
from edc_base.model_validators.date import datetime_not_future
from edc_base.utils import get_utcnow
from edc_identifier.managers import SubjectIdentifierManager
from edc_protocol.validators import datetime_not_before_study_start
from edc_visit_schedule.model_mixins import OffScheduleModelMixin
from edc_visit_schedule.site_visit_schedules import site_visit_schedules

from edc_action_item.model_mixins import ActionModelMixin

from ..action_items import MATERNALOFF_STUDY_ACTION
from ..choices import MATERNAL_OFF_STUDY_REASON
from .offstudy_model_mixin import OffStudyModelMixin


class MaternalOffStudy(OffStudyModelMixin, OffScheduleModelMixin,
                       ActionModelMixin, BaseUuidModel):

    tracking_identifier_prefix = 'MO'

    action_name = MATERNALOFF_STUDY_ACTION

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
        choices=MATERNAL_OFF_STUDY_REASON)

    objects = SubjectIdentifierManager()

    history = HistoricalRecords()

    def take_off_schedule(self):
        maternal_labour_del_schedule = django_apps.get_model(
            'td_maternal.onschedulematernallabourdel')
        antenatal_visit_membership_schedule = django_apps.get_model(
            'td_maternal.onscheduleantenatalvisitmembership')
        antenatal_enrollment_schedule = django_apps.get_model(
            'td_maternal.onscheduleantenatalenrollment')
        maternal_schedules = [maternal_labour_del_schedule,
                              antenatal_visit_membership_schedule,
                              antenatal_enrollment_schedule]

        for on_schedule in maternal_schedules:
            try:
                on_schedule_obj = on_schedule.objects.get(
                    subject_identifier=self.subject_identifier)
            except on_schedule.DoesNotExist:
                pass
            else:
                _, schedule = \
                    site_visit_schedules.get_by_onschedule_model_schedule_name(
                        onschedule_model=on_schedule._meta.label_lower,
                        name=on_schedule_obj.schedule_name)
                schedule.take_off_schedule(offschedule_model_obj=self)

    class Meta:
        app_label = 'td_prn'
        verbose_name = 'Maternal Off Study'
        verbose_name_plural = 'Maternal Off Studies'

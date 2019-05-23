from django.db import models
from edc_base.model_managers import HistoricalRecords
from edc_base.model_mixins import BaseUuidModel
from edc_base.model_validators.date import datetime_not_future
from edc_base.utils import get_utcnow
from edc_identifier.managers import SubjectIdentifierManager
from edc_identifier.model_mixins import TrackingIdentifierModelMixin
from edc_protocol.validators import datetime_not_before_study_start
from edc_visit_schedule.model_mixins import OffScheduleModelMixin
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

    def save(self, *args, **kwargs):
        if not self.last_study_fu_date:
            self.last_study_fu_date = self.offschedule_datetime.date()
        super().save(*args, **kwargs)

    class Meta:
        app_label = 'td_prn'
        verbose_name = "Infant Off-Study"
        verbose_name_plural = "Infant Off-Study"

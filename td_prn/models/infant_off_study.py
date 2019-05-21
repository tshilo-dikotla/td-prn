from django.db import models
from edc_base.model_managers import HistoricalRecords
from edc_base.model_mixins import BaseUuidModel
from edc_identifier.managers import SubjectIdentifierManager
from edc_identifier.model_mixins import TrackingIdentifierModelMixin
from edc_visit_schedule.model_mixins import OffScheduleModelMixin

from ..choices import INFANT_OFF_STUDY_REASON
from .offstudy_model_mixin import OffStudyModelMixin


class InfantOffStudy(OffStudyModelMixin, OffScheduleModelMixin,
                     TrackingIdentifierModelMixin, BaseUuidModel):

    """ A model completed by the user when the infant is taken off study. """

    tracking_identifier_prefix = 'ST'

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
        verbose_name = "Infant Off-Study"
        verbose_name_plural = "Infant Off-Study"

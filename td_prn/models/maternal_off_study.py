from django.db import models
from edc_base.model_managers import HistoricalRecords
from edc_base.model_mixins import BaseUuidModel
from edc_identifier.managers import SubjectIdentifierManager
from edc_visit_schedule.model_mixins import OffScheduleModelMixin

from edc_action_item.model_mixins import ActionModelMixin
from td_maternal.action_items import MATERNALOFF_STUDY_ACTION
from td_maternal.models.model_mixins import ConsentVersionModelModelMixin

from ..choices import MATERNAL_OFF_STUDY_REASON
from .offstudy_model_mixin import OffStudyModelMixin


class MaternalOffStudy(OffStudyModelMixin, ConsentVersionModelModelMixin,
                       OffScheduleModelMixin, ActionModelMixin, BaseUuidModel):

    tracking_identifier_prefix = 'ST'

    reason = models.CharField(
        verbose_name=('Please code the primary reason participant taken'
                      ' off-study'),
        max_length=115,
        choices=MATERNAL_OFF_STUDY_REASON)

    action_name = MATERNALOFF_STUDY_ACTION

    objects = SubjectIdentifierManager()

    history = HistoricalRecords()

    class Meta:
        verbose_name = 'Maternal Off Study'
        verbose_name_plural = 'Maternal Off Studies'

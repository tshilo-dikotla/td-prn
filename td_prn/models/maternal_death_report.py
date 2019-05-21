from django.db import models
from edc_base.model_managers import HistoricalRecords
from edc_base.model_mixins import BaseUuidModel
from edc_base.model_validators import datetime_not_future
from edc_base.sites import SiteModelMixin
from edc_base.utils import get_utcnow
from edc_constants.choices import YES_NO
from edc_identifier.managers import SubjectIdentifierManager
from edc_protocol.validators import datetime_not_before_study_start
from edc_reference.model_mixins import ReferenceModelMixin
from edc_search.model_mixins import SearchSlugModelMixin

from edc_action_item.model_mixins.action_model_mixin import ActionModelMixin
from edc_base.model_fields import OtherCharField
from ..action_items import MATERNAL_DEATH_REPORT_ACTION
from ..choices import MED_RESPONSIBILITY, HOSPITILIZATION_REASONS
from ..choices import SOURCE_OF_DEATH_INFO, CAUSE_OF_DEATH_CAT
from .death_report_model_mixin import DeathReportModelMixin


class MaternalDeathReport(DeathReportModelMixin, ReferenceModelMixin,
                          ActionModelMixin, SiteModelMixin,
                          SearchSlugModelMixin, BaseUuidModel):

    tracking_identifier_prefix = 'MDR'

    action_name = MATERNAL_DEATH_REPORT_ACTION

    objects = SubjectIdentifierManager()

    history = HistoricalRecords()

    def natural_key(self):
        return (self.subject_identifier,)

    natural_key.dependencies = ['sites.Site']

    class Meta:
        verbose_name = 'Maternal Death Report'

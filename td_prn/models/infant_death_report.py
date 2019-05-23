from django.db import models
from edc_base.model_mixins import BaseUuidModel
from edc_base.sites import SiteModelMixin
from edc_search.model_mixins import SearchSlugModelMixin

from edc_action_item.model_mixins.action_model_mixin import ActionModelMixin
from edc_base.model_fields import OtherCharField

from ..action_items import INFANT_DEATH_REPORT_ACTION
from ..choices import RELATIONSHIP_CHOICES
from .death_report_model_mixin import DeathReportModelMixin


class InfantDeathReport(DeathReportModelMixin, ActionModelMixin,
                        SiteModelMixin, SearchSlugModelMixin, BaseUuidModel):

    ''' A model completed by the user after an infant's death. '''

    tracking_identifier_prefix = 'ID'

    action_name = INFANT_DEATH_REPORT_ACTION

    study_drug_relationship = models.CharField(
        verbose_name=('Relationship between the infant\'s death and '
                      '(CTX vs Placebo) '),
        max_length=20,
        choices=RELATIONSHIP_CHOICES)

    infant_nvp_relationship = models.CharField(
        verbose_name=('Relationship between the infant\'s death and '
                      'infant extended nevirapine prophylaxis '),
        max_length=20,
        choices=RELATIONSHIP_CHOICES)

    haart_relationship = models.CharField(
        verbose_name=('Relationship between the infant\'s death and '
                      'HAART '),
        max_length=20,
        choices=RELATIONSHIP_CHOICES)

    trad_med_relationship = models.CharField(
        verbose_name=('Relationship between the infant\'s death and '
                      'traditional medicine use '),
        max_length=20,
        choices=RELATIONSHIP_CHOICES)

    class Meta:
        app_label = 'td_prn'
        verbose_name = 'Infant Death Report'

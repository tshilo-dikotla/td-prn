from django.db import models
from edc_base.model_mixins import BaseUuidModel
from edc_base.model_validators import datetime_not_future
from edc_base.sites import SiteModelMixin
from edc_base.utils import get_utcnow
from edc_constants.choices import YES_NO
from edc_identifier.model_mixins import UniqueSubjectIdentifierFieldMixin
from edc_protocol.validators import datetime_not_before_study_start
from edc_search.model_mixins import SearchSlugModelMixin

from edc_base.model_fields import OtherCharField

from ..choices import CAUSE_OF_DEATH, CAUSE_OF_DEATH_CAT, MED_RESPONSIBILITY
from ..choices import HOSPITILIZATION_REASONS, SOURCE_OF_DEATH_INFO
from ..choices import RELATIONSHIP_CHOICES


class InfantDeathReport(UniqueSubjectIdentifierFieldMixin, SiteModelMixin,
                        SearchSlugModelMixin, BaseUuidModel):

    """ A model completed by the user after an infant's death. """

    report_datetime = models.DateTimeField(
        verbose_name='Report Date',
        validators=[
            datetime_not_before_study_start,
            datetime_not_future],
        default=get_utcnow)

    death_date = models.DateField(
        validators=[datetime_not_future],
        verbose_name='Date of Death:')

    comment = models.TextField(
        max_length=500,
        verbose_name="Comments",
        blank=True,
        null=True)

    cause = models.CharField(
        max_length=100,
        choices=SOURCE_OF_DEATH_INFO,
        verbose_name=('what is the primary source of '
                      ' cause of death information? '
                      '(if multiple source of information, '
                      'list one with the smallest number closest to the top of the list)'))

    cause_other = OtherCharField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name='If "Other" above, please specify')

    diagnosis_code = models.CharField(
        max_length=50,
        choices=CAUSE_OF_DEATH,
        verbose_name=('Main cause of death'),
        help_text=('Main cause of death in the opinion of the '
                   ' local study doctor and local PI'))

    diagnosis_code_other = OtherCharField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name='If "Other" above, please specify')

    cause_category = models.CharField(
        max_length=50,
        choices=CAUSE_OF_DEATH_CAT,
        verbose_name=('based on the above description, what category best '
                      'defines the major cause of death?'))

    cause_category_other = OtherCharField(
        verbose_name='If "Other" above, please specify',
        blank=True,
        null=True)

    perform_autopsy = models.CharField(
        max_length=3,
        choices=YES_NO,
        verbose_name='Will an autopsy be performed later')

    medical_responsibility = models.CharField(
        choices=MED_RESPONSIBILITY,
        max_length=50,
        verbose_name='Who was responsible for primary medical care of the '
        'participant during the month prior to death?',
        help_text="")

    participant_hospitalized = models.CharField(
        max_length=3,
        choices=YES_NO,
        verbose_name="Was the participant hospitalised before death?")

    reason_hospitalized = models.CharField(
        choices=HOSPITILIZATION_REASONS,
        max_length=50,
        verbose_name='if yes, hospitalized, what was the primary reason for hospitalisation? ',
        blank=True,
        null=True)

    reason_hospitalized_other = models.TextField(
        verbose_name='if other illness or pathogen specify or non '
        'infectious reason, please specify below:',
        max_length=250,
        blank=True,
        null=True)

    days_hospitalized = models.IntegerField(
        verbose_name=(
            'For how many days was the participant hospitalised during '
            'the illness immediately before death? '),
        help_text="in days",
        default=0)

    death_cause = models.TextField(
        verbose_name=(
            'Describe the major cause of death (including pertinent autopsy information '
            'if available), starting with the first noticeable illness thought to be '
            'related to death, continuing to time of death.'),
        blank=True,
        null=True,
        help_text=(
            'Note: Cardiac and pulmonary arrest are not major reasons and should not '
            'be used to describe major cause'))

    illness_duration = models.IntegerField(
        verbose_name='Duration of acute illness directly causing death   ',
        help_text='in days (If unknown enter -1)')

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
        app_label = 'td_infant'
        verbose_name = "Infant Death Report"

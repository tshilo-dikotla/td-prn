from edc_constants.constants import (
    OFF_STUDY, ON_STUDY, FAILED_ELIGIBILITY, PARTICIPANT)
from edc_constants.constants import ALIVE, DEAD, NOT_APPLICABLE, OTHER, UNKNOWN
from edc_visit_tracking.constants import MISSED_VISIT, COMPLETED_PROTOCOL_VISIT
from edc_visit_tracking.constants import SCHEDULED, UNSCHEDULED, LOST_VISIT

from td_maternal.constants import NO_MODIFICATIONS, START

from .constants import BREASTFEED_ONLY, NEVER_STARTED, MODIFIED, TUBERCULOSIS
from .constants import MIN_AGE_OF_CONSENT

CAUSE_OF_DEATH_CAT = (
    ('hiv_related', 'HIV infection or HIV related diagnosis'),
    ('hiv_unrelated', 'Disease unrelated to HIV'),
    ('study_drug', 'Toxicity from Study Drug'),
    ('non_study_drug', 'Toxicity from non-Study drug'),
    ('trauma', 'Trauma/Accident'),
    ('no_info', 'No information available'),
    (OTHER, 'Other, specify'),)

CAUSE_OF_DEATH = (
    ('cryptococcal_meningitis', 'Cryptococcal meningitis'),
    ('Cryptococcal_meningitis_relapse_IRIS',
     'Cryptococcal meningitis relapse/IRIS'),
    (TUBERCULOSIS, 'TB'),
    ('bacteraemia', 'Bacteraemia'),
    ('bacterial_pneumonia', 'Bacterial pneumonia'),
    ('malignancy', 'Malignancy'),
    ('art_toxicity', 'ART toxicity'),
    ('IRIS_non_CM', 'IRIS non-CM'),
    ('diarrhea_wasting', 'Diarrhea/wasting'),
    (UNKNOWN, 'Unknown'),
    (OTHER, 'Other'),
)

HOSPITILIZATION_REASONS = (
    ('respiratory illness(unspecified)', 'Respiratory Illness(unspecified)'),
    ('respiratory illness, cxr confirmed',
     'Respiratory Illness, CXR confirmed'),
    ('respiratory illness, cxr confirmed, bacterial pathogen, specify',
     'Respiratory Illness, CXR confirmed, bacterial pathogen, specify'),
    ('respiratory illness, cxr confirmed, tb or probable tb',
     'Respiratory Illness, CXR confirmed, TB or probable TB'),
    ('diarrhea illness(unspecified)', 'Diarrhea Illness(unspecified)'),
    ('diarrhea illness, viral or bacterial pathogen, specify',
     'Diarrhea Illness, viral or bacterial pathogen, specify'),
    ('sepsis(unspecified)', 'Sepsis(unspecified)'),
    ('sepsis, pathogen specified, specify',
     'Sepsis, pathogen specified, specify'),
    ('mengitis(unspecified)', 'Mengitis(unspecified)'),
    ('mengitis, pathogen specified, specify',
     'Mengitis, pathogen specified, specify'),
    ('non-infectious reason for hospitalization, specify',
     'Non-infectious reason for hospitalization, specify'),
    (OTHER, 'Other infection, specify'),
)

INFANT_OFF_STUDY_REASON = (
    ('not_18'.format(MIN_AGE_OF_CONSENT),
     f' Mother of infant found to be less than {MIN_AGE_OF_CONSENT} '
     'years of age'),
    ('not_citizen', ' Mother found not be a citizen of Botswana'),
    ('moved',
     ' Subject will be moving out of study area or unable to stay '
     'in study area'),
    ('lost_no_contact', ' Lost to follow-up, unable to locate'),
    ('lost_contacted',
     ' Lost to follow-up, contacted but did not come to study clinic'),
    ('withdrew_by_mother',
     ' Mother changed mind and withdrew consent'),
    ('withdrew_by_father',
     ' Father of baby did not want infant to participate and participant'
     ' withdrew consent'),
    ('withdrew_by_family',
     ' Other family member did not want mother/infant to participate and'
     ' participant withdrew consent'),
    ('hiv_pos', ' Infant found to be HIV-infected'),
    ('ill',
     ' Infant diagnosed with medical condition making survival to 12 months'
     ' unlikely'),
    ('complete',
     (' Completion of protocol required period of time for observation'
      ' (see Study Protocol for definition of Completion.)'
      ' [skip to end of form]')),
    ('death',
     (' Participant death (complete the DEATH REPORT FORM AF005) (For '
      'EAE Reporting requirements see EAE Reporting Manual)')),
    (OTHER, ' Other'),
)

MATERNAL_OFF_STUDY_REASON = (
    ('multiple_vialble_gestations',
     'Multiple (2 or more) viable gestations seen on ultrasound'),
    ('miscarriage_or_arbotion_lt_20wks',
     'Miscarriage or arbotion (fetal demise < 20 weeks GA)'),
    ('fetal_death_gt_20wks',
     'fetal Death at >= 20weeks GA (IUFD) or still born'),
    ('maternal_seroconversion_gt_33wks',
     'Maternal seroconversion after 33 weeks GA'),
    ('took_art_less_than_4weeks',
     'Mother took ART for less than 4 weeks during pregnancy'),
    ('maternal_death_pre_deliv',
     'Maternal death PRIOR to delivery (complete the Death Report '
     'Form AF005)'),
    ('maternal_death_post_deliv',
     'Maternal death POST delivery (complete the Death Report Form AF005)'),
    ('moving_out_of_study_area_pre_deliv',
     'Participant stated she will be moving out of the study area or '
     'unable to stay in study area PRIOR delivery'),
    ('moving_out_of_study_area_post_deliv',
     'Participant stated she will be moving out of the study area or '
     'unable to stay in study area POST delivery'),
    ('loss_to_followup_prior_deliv',
     'Participant lost to follow-up/unable to locate PRIOR to delivery'),
    ('loss_to_followup_post_deliv',
     'Participant lost to follow-up/unable to locate POST to delivery'),
    ('loss_to_followup_contacted_prior_deliv',
     'Participant lost to follow-up, contacted but did not come to study '
     'clinic PRIOR to delivery'),
    ('loss_to_followup_contacted_post_deliv',
     'Participant lost to follow-up, contacted but did not come to study '
     'clinic POST to delivery'),
    ('withdrew_consent_prior_deliv',
     'Mother changed mind and withdrew consent PRIOR to delivery'),
    ('withdrew_consent_post_deliv',
     'Mother changed mind and withdrew consent POST to delivery'),
    ('father_refused_prior_deliv',
     'Father of the baby refused to participate, hence participant '
     'withdrew consent PRIOR delivery'),
    ('father_refused_post_deliv',
     'Father of the baby refused to participate, hence participant '
     'withdrew consent POST delivery'),
    ('family_member_refused_prior_deliv',
     'Other family member refused to participate, hence participant '
     'withdrew consent PRIOR delivery'),
    ('family_member_refused_post_deliv',
     'Other family member refused to participate, hence participant '
     'withdrew consent POST delivery'),
    ('infant_hiv_infected', 'Infant found to be HIV infected'),
    ('infant_death', 'Infant death (complete infant Death Report Form)'),
    ('protocol_completion',
     'Completion of protocol required period of time for observation '
     '(see Study Protocol for definition of'
     ' "Completion") (skip to end of form)'),
    ('unable_to_determine_ga', 'Unable to confirm GA by Ultrasound.'),
    ('enrolled_erroneously',
     'Enrolled erroneously – did not meet eligibility criteria'),
    ('mother_not_complete_anv1', 'Mother did not complete ANV1 (1010) visit.'),
    (OTHER, 'Other'),
)

MED_RESPONSIBILITY = (
    ('doctor', 'Doctor'),
    ('nurse', 'Nurse'),
    ('traditional', 'Traditional Healer'),
    ('all', 'Both Doctor or Nurse and Traditional Healer'),
    ('none', 'No known medical care received (family/friends only)'),)

SOURCE_OF_DEATH_INFO = (
    ('autopsy', 'Autopsy'),
    ('clinical_records', 'Clinical_records'),
    ('study_staff',
     'Information from study care taker staff prior participant death'),
    ('health_care_provider',
     'Contact with other (non-study) physician/nurse/other health care provider'),
    ('death_certificate', 'Death Certificate'),
    ('relatives_friends',
     'Information from participant\'s relatives or friends'),
    ('obituary', 'Obituary'),
    ('pending_information', 'Information requested, still pending'),
    ('no_info', 'No information will ever be available'),
    (OTHER, 'Other, specify'),)

RELATIONSHIP_CHOICES = (
    ('Not related', 'Not related'),
    ('Probably not related', 'Probably not related'),
    ('Possibly related', 'Possibly related'),
    ('Probably related', 'Probably related'),
    ('Definitely related', 'Definitely related'),
)

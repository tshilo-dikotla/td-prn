from edc_constants.constants import YES
from edc_form_validators import FormValidator

from ..constants import OTHER


class DeathReportFormValidator(FormValidator):

    def clean(self):

        self.m2m_other_specify(
            OTHER,
            m2m_field='cause',
            field_other='cause_other')

        self.m2m_other_specify(
            OTHER,
            m2m_field='cause_category',
            field_other='cause_category_other')

        self.required_if(
            YES,
            field='participant_hospitalized',
            field_required='reason_hospitalized')

        self.m2m_other_specify(
            OTHER,
            m2m_field='reason_hospitalized',
            field_other='reason_hospitalized_other')

        self.required_if(
            YES,
            field='participant_hospitalized',
            field_required='days_hospitalized')

        self.m2m_other_specify(
            OTHER,
            m2m_field='diagnosis_code',
            field_other='diagnosis_code_other')

from edc_constants.constants import YES
from edc_form_validators import FormValidator


class DeathReportFormValidator(FormValidator):

    def clean(self):

        self.validate_other_specify(
            field='cause',
            other_specify_field='cause_other')

        self.validate_other_specify(
            field='cause_category',
            other_specify_field='cause_category_other')

        self.required_if(
            YES,
            field='participant_hospitalized',
            field_required='reason_hospitalized')

        self.validate_other_specify(
            field='reason_hospitalized',
            other_specify_field='reason_hospitalized_other')

        self.required_if(
            YES,
            field='participant_hospitalized',
            field_required='days_hospitalized')

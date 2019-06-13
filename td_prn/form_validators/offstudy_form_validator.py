from edc_form_validators import FormValidator
from td_maternal_validators.form_validators.form_validator_mixin import (
    TDFormValidatorMixin)


class OffstudyFormValidator(TDFormValidatorMixin, FormValidator):

    def clean(self):
        super().clean()
        self.subject_identifier = self.cleaned_data.get('subject_identifier')

        self.validate_other_specify(
            field='reason',
            other_specify_field='reason_other',
        )

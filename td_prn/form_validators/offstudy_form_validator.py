from edc_form_validators import FormValidator


class OffstudyFormValidator(FormValidator):

    def clean(self):

        self.validate_other_specify(
            field='reason',
            other_specify_field='reason_other',
        )

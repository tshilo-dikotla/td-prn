from django import forms
from edc_form_validators import FormValidatorMixin
from td_maternal_validators.form_validators.form_validator_mixin import (
    TDFormValidatorMixin)

from ..form_validators import OffstudyFormValidator
from ..models import MaternalOffStudy


class MaternalOffStudyForm(FormValidatorMixin, forms.ModelForm):

    form_validator_cls = OffstudyFormValidator

    def clean(self):
        super().clean()

    class Meta:
        model = MaternalOffStudy
        fields = '__all__'

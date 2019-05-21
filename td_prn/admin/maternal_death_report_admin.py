from django.contrib import admin
from edc_model_admin import audit_fieldset_tuple
from ..admin_site import td_prn_admin
from ..forms import MaternalDeathReportForm
from ..models import MaternalDeathReport
from .modeladmin_mixins import ModelAdminMixin


@admin.register(MaternalDeathReport, site=td_prn_admin)
class MaternalDeathReportAdmin(ModelAdminMixin, admin.ModelAdmin):

    form = MaternalDeathReportForm

    fieldsets = (
        (None, {
            'fields': [
                'subject_identifier',
                'report_datetime',
                'death_date',
                'cause',
                'cause_other',
                'perform_autopsy',
                'death_cause',
                'cause_category',
                'cause_category_other',
                'illness_duration',
                'medical_responsibility',
                'participant_hospitalized',
                'reason_hospitalized',
                'reason_hospitalized_other',
                'days_hospitalized',
                'comment', ]}
         ), audit_fieldset_tuple)

    radio_fields = {
        'cause': admin.VERTICAL,
        'cause_category': admin.VERTICAL,
        'perform_autopsy': admin.VERTICAL,
        'medical_responsibility': admin.VERTICAL,
        'participant_hospitalized': admin.VERTICAL,
        'reason_hospitalized': admin.VERTICAL}

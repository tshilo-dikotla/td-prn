from django.conf import settings
from django.contrib import admin
from django_revision.modeladmin_mixin import ModelAdminRevisionMixin
from edc_base.sites.admin import ModelAdminSiteMixin
from edc_metadata import NextFormGetter
from edc_model_admin import (
    ModelAdminNextUrlRedirectMixin, ModelAdminFormInstructionsMixin,
    ModelAdminFormAutoNumberMixin, ModelAdminAuditFieldsMixin,
    ModelAdminReadOnlyMixin, ModelAdminInstitutionMixin,
    ModelAdminRedirectOnDeleteMixin)
from edc_model_admin import audit_fieldset_tuple
from edc_subject_dashboard import ModelAdminSubjectDashboardMixin

from ..admin_site import td_prn_admin
from ..forms import InfantDeathReportForm
from ..models import InfantDeathReport
from .exportaction_mixin import ExportActionMixin


class ModelAdminMixin(ModelAdminNextUrlRedirectMixin,
                      ModelAdminFormInstructionsMixin,
                      ModelAdminFormAutoNumberMixin, ModelAdminRevisionMixin,
                      ModelAdminAuditFieldsMixin, ModelAdminReadOnlyMixin,
                      ModelAdminInstitutionMixin,
                      ModelAdminRedirectOnDeleteMixin,
                      ModelAdminSubjectDashboardMixin, ExportActionMixin,
                      ModelAdminSiteMixin):

    list_per_page = 10
    date_hierarchy = 'modified'
    empty_value_display = '-'
    next_form_getter_cls = NextFormGetter
    subject_dashboard_url = 'infant_subject_dashboard_url'

    post_url_on_delete_name = settings.DASHBOARD_URL_NAMES.get(
        subject_dashboard_url)

    def post_url_on_delete_kwargs(self, request, obj):
        return dict(subject_identifier=obj.subject_identifier)


@admin.register(InfantDeathReport, site=td_prn_admin)
class InfantDeathReportAdmin(ModelAdminMixin, admin.ModelAdmin):

    form = InfantDeathReportForm

    search_fields = ('subject_identifier',)

    fieldsets = (
        (None, {
            'fields': (
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
                'study_drug_relationship',
                'infant_nvp_relationship',
                'haart_relationship',
                'trad_med_relationship',
                'comment')}),
        audit_fieldset_tuple
    )

    radio_fields = {
        'reason_hospitalized': admin.VERTICAL,
        'medical_responsibility': admin.VERTICAL,
        'cause': admin.VERTICAL,
        'cause_category': admin.VERTICAL,
        'perform_autopsy': admin.VERTICAL,
        'participant_hospitalized': admin.VERTICAL,
        'study_drug_relationship': admin.VERTICAL,
        'infant_nvp_relationship': admin.VERTICAL,
        'haart_relationship': admin.VERTICAL,
        'trad_med_relationship': admin.VERTICAL
    }

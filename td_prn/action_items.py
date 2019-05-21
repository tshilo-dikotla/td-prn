from django.apps import apps as django_apps
from django.core.exceptions import ObjectDoesNotExist
from edc_action_item import Action, site_action_items, HIGH_PRIORITY

MATERNALOFF_STUDY_ACTION = 'submit-maternaloff-study'
MATERNAL_DEATH_REPORT_ACTION = 'submit-maternal-death-report'


class MaternalOffStudyAction(Action):
    name = MATERNALOFF_STUDY_ACTION
    display_name = 'Submit Maternal Offstudy'
    reference_model = 'td_prn.maternaloffstudy'
    admin_site_name = 'td_prn_admin'
    priority = HIGH_PRIORITY
    singleton = True


class MaternalDeathReportAction(Action):
    name = MATERNAL_DEATH_REPORT_ACTION
    display_name = 'Submit Maternal Death Report'
    reference_model = 'td_prn.maternaldeathreport'
    admin_site_name = 'td_prn_admin'
    priority = HIGH_PRIORITY
    singleton = True

    def get_next_actions(self):
        actions = []
        maternal_deathreport_cls = django_apps.get_model(
            'td_prn.maternaldeathreport')

        subject_identifier = self.reference_model_obj.subject_identifier
        try:
            maternal_deathreport_cls.objects.get(
                subject_identifier=subject_identifier)
            actions = [MaternalOffStudyAction]
        except ObjectDoesNotExist:
            pass
        return actions


site_action_items.register(MaternalDeathReportAction)
site_action_items.register(MaternalOffStudyAction)

from django.apps import apps as django_apps
from django.core.exceptions import ObjectDoesNotExist
from edc_action_item import Action, site_action_items, HIGH_PRIORITY

MATERNALOFF_STUDY_ACTION = 'submit-maternaloff-study'
INFANTOFF_STUDY_ACTION = 'submit-infantoff-study'
MATERNAL_DEATH_REPORT_ACTION = 'submit-maternal-death-report'
INFANT_DEATH_REPORT_ACTION = 'submit-infant-death-report'


class MaternalOffStudyAction(Action):
    name = MATERNALOFF_STUDY_ACTION
    display_name = 'Submit Maternal Offstudy'
    reference_model = 'td_prn.maternaloffstudy'
    admin_site_name = 'td_prn_admin'
    priority = HIGH_PRIORITY
    singleton = True


class InfantOffStudyAction(Action):
    name = INFANTOFF_STUDY_ACTION
    display_name = 'Submit Infant Offstudy'
    reference_model = 'td_prn.infantoffstudy'
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
        offstudy = None
        maternal_deathreport_cls = django_apps.get_model(
            'td_prn.maternaldeathreport')

        action_item_cls = django_apps.get_model(
            'edc_action_item.actionitem')

        subject_identifier = self.reference_model_obj.subject_identifier
        offstudy = action_item_cls.objects.filter(
            subject_identifier=subject_identifier,
            action_type__name='submit-maternaloff-study')
        try:
            maternal_deathreport_cls.objects.get(
                subject_identifier=subject_identifier)
            if not offstudy:
                actions = [MaternalOffStudyAction]
        except ObjectDoesNotExist:
            pass
        return actions


class InfantDeathReportAction(Action):
    name = INFANT_DEATH_REPORT_ACTION
    display_name = 'Submit Infant Death Report'
    reference_model = 'td_prn.infantdeathreport'
    admin_site_name = 'td_prn_admin'
    priority = HIGH_PRIORITY
    singleton = True


site_action_items.register(MaternalDeathReportAction)
site_action_items.register(MaternalOffStudyAction)
site_action_items.register(InfantDeathReportAction)
site_action_items.register(InfantOffStudyAction)

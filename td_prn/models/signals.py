from django.db.models.signals import post_save
from django.dispatch import receiver
from edc_visit_schedule.site_visit_schedules import site_visit_schedules
from edc_visit_schedule.subject_schedule import NotOnScheduleError

from .maternal_off_study import MaternalOffStudy


@receiver(post_save, weak=False, sender=MaternalOffStudy,
          dispatch_uid='maternal_off_study_on_post_save')
def study_termination_conclusion_on_post_save(sender, instance, raw, created, **kwargs):

    if not raw:

        try:
            onschedule_models = ['td_maternal.onscheduleantenatalenrollment',
                                 'td_maternal.onscheduleantenatalvisitmembership',
                                 'td_maternal.onschedulematernallabourdel']
            print('************************************')
            print('taking participant off study')
            print('************************************')
#             for onschedule_model in onschedule_models:
#                 _, schedule = site_visit_schedules.get_by_onschedule_model(
#                     onschedule_model)
            _, schedule = site_visit_schedules.get_by_onschedule_model_schedule_name(
                'td_maternal.onscheduleantenatalenrollment', name='antenatal_schedule_3')
#                 if schedule.is_onschedule(instance.subject_identifier):
            print(schedule)
            schedule.take_off_schedule(
                offschedule_model_obj=instance,
                offschedule_datetime=instance.offstudy_date,
                subject_identifier=instance.subject_identifier)
            print('************************************')
            print(schedule)
            print('************************************')

        except AttributeError:
            pass


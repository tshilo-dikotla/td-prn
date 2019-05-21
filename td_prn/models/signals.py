from django.db.models.signals import post_save
from django.dispatch import receiver
from edc_visit_schedule.site_visit_schedules import site_visit_schedules

from td_maternal.models.onschedule import OnScheduleAntenatalEnrollment
from td_maternal.models.onschedule import OnScheduleAntenatalVisitMembership
from td_maternal.models.onschedule import OnScheduleMaternalLabourDel

from .maternal_off_study import MaternalOffStudy


@receiver(post_save, weak=False, sender=MaternalOffStudy,
          dispatch_uid='maternal_off_study_on_post_save')
def maternal_offstudy_on_post_save(sender, instance, raw, created, **kwargs):

    if not raw:
        take_off_schedule(instance)


def take_off_schedule(self, instance):
    maternal_schedules = [OnScheduleMaternalLabourDel,
                          OnScheduleAntenatalVisitMembership,
                          OnScheduleAntenatalEnrollment]

    for on_schedule in maternal_schedules:
        try:
            on_schedule_obj = on_schedule.objects.get(
                subject_identifier=instance.subject_identifier)
        except on_schedule.DoesNotExist:
            pass
        else:
            _, schedule = \
                site_visit_schedules.get_by_onschedule_model_schedule_name(
                    onschedule_model=on_schedule._meta.label_lower,
                    name=on_schedule_obj.schedule_name)
            schedule.take_off_schedule(offschedule_model_obj=self)

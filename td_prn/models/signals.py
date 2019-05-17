from django.db.models.signals import post_save
from django.dispatch import receiver

from .maternal_off_study import MaternalOffStudy


@receiver(post_save, weak=False, sender=MaternalOffStudy,
          dispatch_uid='maternal_off_study_on_post_save')
def study_termination_conclusion_on_post_save(sender, instance, raw, created, **kwargs):

    if not raw:
        instance.take_off_schedule()

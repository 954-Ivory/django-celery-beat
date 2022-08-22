def signals_connect():
    from django.db.models import signals
    from .models import ClockedSchedule, PeriodicTask, PeriodicTasks, IntervalSchedule, CrontabSchedule, SolarSchedule

    signals.pre_delete.connect(PeriodicTasks.changed, sender=PeriodicTask)
    signals.pre_save.connect(PeriodicTasks.changed, sender=PeriodicTask)
    signals.pre_delete.connect(
        PeriodicTasks.update_changed, sender=IntervalSchedule)
    signals.post_save.connect(
        PeriodicTasks.update_changed, sender=IntervalSchedule)
    signals.post_delete.connect(
        PeriodicTasks.update_changed, sender=CrontabSchedule)
    signals.post_save.connect(
        PeriodicTasks.update_changed, sender=CrontabSchedule)
    signals.post_delete.connect(
        PeriodicTasks.update_changed, sender=SolarSchedule)
    signals.post_save.connect(
        PeriodicTasks.update_changed, sender=SolarSchedule)
    signals.post_delete.connect(
        PeriodicTasks.update_changed, sender=ClockedSchedule)
    signals.post_save.connect(
        PeriodicTasks.update_changed, sender=ClockedSchedule)

from rx.subject import Subject
from singleton_decorator import singleton


@singleton
class SchedulerEvent:

    def __init__(self):
        self._add_job_subject = Subject()
        self._start_scheduler_subject = Subject()

    def fire_start_scheduler_event(self, start=True):
        self._start_scheduler_subject.on_next(start)

    def subscribe_start_scheduler_event(self, callback):
        self._start_scheduler_subject.subscribe(callback)

    def fire_add_job_event(self, job):
        self._add_job_subject.on_next(job)

    def subscribe_add_job_event(self, callback):
        self._add_job_subject.subscribe(callback)

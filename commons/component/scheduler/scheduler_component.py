from commons.component import Component
from commons.component.scheduler.scheduler_event import SchedulerEvent
from commons.job_scheduler import IntervalJob
from commons.job_scheduler.job_scheduler import JobScheduler


class SchedulerComponent(Component):

    def __init__(self):
        super().__init__()
        self.scheduler = JobScheduler()
        self.scheduler_event = SchedulerEvent()

    def start(self):
        self.scheduler_event.subscribe_start_scheduler_event(self.start_scheduler)
        self.scheduler_event.subscribe_add_job_event(self.add_interval_job)

    def add_interval_job(self, interval_job):
        if not isinstance(interval_job, IntervalJob):
            raise TypeError("interval job is not of type", IntervalJob)
        job = interval_job.job
        interval = interval_job.interval
        self.scheduler.add_interval_job(job, interval)

    def remove_job(self):
        pass

    def start_scheduler(self, start=True):
        self.scheduler.start()

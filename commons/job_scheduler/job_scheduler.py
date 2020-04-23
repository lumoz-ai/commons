from apscheduler.schedulers.background import BackgroundScheduler
from singleton_decorator import singleton
from commons.utils import create_uuid


@singleton
class JobScheduler:
    def __init__(self):
        self.scheduler = BackgroundScheduler()

    def add_interval_job(self, job, interval):
        job_id = create_uuid()
        self.scheduler.add_job(job, 'interval', seconds=interval, id=job_id)

    def start(self):
        self.scheduler.start()

    def shutdown(self):
        self.scheduler.shutdown()

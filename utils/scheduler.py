"""
Scheduler functions that schedule our periodic jobs.
"""
import logging
from datetime import datetime, timedelta

from apscheduler.schedulers.background import BackgroundScheduler
from inserter.event_inserter import initialize_event_inserter


# Scheduling the periodic job that reads the DataQueue fed by mqtt client, validates it and inserts the data into db"""
def schedule_jobs(**kwargs):
    logging.info("scheduling inserter job")
    scheduler = BackgroundScheduler()
    scheduler.add_job(
        initialize_event_inserter,
        'interval',
        seconds=5,
        next_run_time=datetime.now() + timedelta(seconds=5),
        replace_existing=True,
        kwargs={'mongo_db': kwargs['mongo_db'], 'validators_by_schema_name': kwargs['validators_by_schema_name']},
        max_instances=1
    )
    scheduler.start()

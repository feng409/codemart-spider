import asyncio
from datetime import datetime, timedelta


from apscheduler.events import EVENT_JOB_EXECUTED, EVENT_JOB_ERROR
from apscheduler.schedulers.asyncio import AsyncIOScheduler

from code_mart import spider
from work_schedule import work_schedule
from util import _logger


def run():
    spider()
    work_schedule()


def execution_listener(event):
    if event.exception:
        _logger.error('The job crashed')
    else:
        # check that the executed job is the first job
        job = scheduler.get_job(event.job_id)
        if getattr(job, 'name', '') == 'spider':
            scheduler.add_job(work_schedule, name='work_schedule')


if __name__ == '__main__':
    scheduler = AsyncIOScheduler()
    scheduler.add_job(spider, trigger='interval', minutes=1, name='spider',
                      next_run_time=datetime.now() + timedelta(seconds=4))
    scheduler.add_listener(callback=execution_listener, mask=EVENT_JOB_EXECUTED | EVENT_JOB_ERROR)
    scheduler.start()

    # Execution will block here until Ctrl+C (Ctrl+Break on Windows) is pressed.
    try:
        asyncio.get_event_loop().run_forever()
    except (KeyboardInterrupt, SystemExit):
        pass

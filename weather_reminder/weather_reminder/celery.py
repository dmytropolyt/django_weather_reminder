from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from django.conf import settings
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'weather_reminder.settings')

app = Celery('weather_reminder')
# app.conf.enable_utc = False
# app.conf.update(timezone='Asia/Kolkata')

app.config_from_object(settings, namespace='CELERY')

# app.conf.beat_schedule = {
#     'send_mail_1_hours': {
#         'task': 'sendmail.tasks.send_mail_task',
#         'schedule': crontab(minute=1) #every 30 seconds it will be called
#         #'args': (2,) you can pass arguments also if rquired
#     },
#     'send_mail_3_hours': {
#         'task': 'sendmail.tasks.send_mail_task',
#         'schedule': crontab(hour=3, minute=0)
#     },
#     'send_mail_6_hours': {
#         'task': 'sendmail.tasks.send_mail_task',
#         'schedule': crontab(hour=6, minute=0)
#     },
#     'send_mail_12_hours': {
#         'task': 'sendmail.tasks.send_mail_task',
#         'schedule': crontab(hour=12, minute=0)
#     }
# }
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
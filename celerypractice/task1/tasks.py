from celery import shared_task
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.conf import settings
from celery.exceptions import SoftTimeLimitExceeded, TimeLimitExceeded
import time


@shared_task(bind=True, soft_time_limit=10, time_limit=20)
def send_mail_func(self):
    try:
        time.sleep(30)
    except SoftTimeLimitExceeded:
        print("work")
        raise TimeLimitExceeded

from celery import shared_task
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.conf import settings
from celery.exceptions import SoftTimeLimitExceeded, TimeLimitExceeded
import time
from .decorator import decorator1


@shared_task(bind=True, soft_time_limit=10, time_limit=20)
@decorator1
def send_mail_func(self, id):
    print(id)
    time.sleep(30)
    return

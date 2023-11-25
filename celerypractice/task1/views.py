from .tasks import send_mail_func
from django.http import HttpResponse


def send_mail_view(request):
    send_mail_func.apply_async((3,), time_limit=30, soft_time_limit=20)
    return HttpResponse("sent")

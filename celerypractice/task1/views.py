from .tasks import send_mail_func
from django.http import HttpResponse


def send_mail_view(request):
    send_mail_func.delay()
    return HttpResponse("sent")

from django.urls import path
from .views import send_mail_view

urlpatterns = [
    path("", view=send_mail_view)
]

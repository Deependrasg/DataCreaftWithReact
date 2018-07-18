from django.core.mail import send_mail
import os
from decouple import config
from celery import shared_task

@shared_task
def send_varification_email(subject, message, email):
    send_mail(
        subject,
        message,
        config('EMAIL_HOST_USER'),
        [email],
        html_message=message
    )

@shared_task
def welcome_note(subject, message, email):
    send_mail(
        subject,
        message,
        config('EMAIL_HOST_USER'),
        [email],
        html_message=message
    )

@shared_task
def success_full(subject, message, email):
    send_mail(
        subject,
        message,
        config('EMAIL_HOST_USER'),
        [email],
        html_message=message
    )
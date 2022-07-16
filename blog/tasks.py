from celery import shared_task
from django.conf import settings
from django.core.mail import EmailMessage

from blog.models import Subscription


@shared_task
def send_blog_email(subject, message):
    """Sends notification emails to all subscribers"""

    subscribers = Subscription.objects.values_list('email', flat=True)
    emails = EmailMessage(
        subject,
        message,
        settings.EMAIL_HOST_USER,
        subscribers,
    )
    return emails.send()

from celery.utils.log import get_task_logger
from django.conf import settings
from django.core.mail import send_mail

from DRFRocketloop.celery import app


@app.task
def send_mail_task(recipients, subject, context):
    logger = get_task_logger(__name__)
    send_mail(
        subject=subject,
        message=context,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=recipients,
        fail_silently=False,
        html_message=context
    )
    logger.info('Email sent')

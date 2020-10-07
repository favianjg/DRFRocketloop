from django.core.mail import send_mail

from DRFRocketloop.celery import app


@app.task
def send_mail_task(recipients, subject, context):
    send_mail(
        subject=subject,
        message=context,
        from_email="rafcath95@gmail.com",
        recipient_list=recipients,
        fail_silently=False,
        html_message=context
    )

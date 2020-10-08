from datetime import datetime, timedelta

from pytz import timezone
from rest_framework import viewsets

from reminder.models import Reminders
from reminder.sendmail_task import send_mail_task
from reminder.serializers import ReminderSerializer


# Create your views here.
class ReminderViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """

    queryset = Reminders.objects.all()
    serializer_class = ReminderSerializer

    def perform_create(self, serializer):
        if serializer.is_valid():
            validatedData = serializer.validated_data
            email = validatedData.get('email')
            subject = "Reminder from DRFRocketLoop"
            text = validatedData.get('text')
            minute = validatedData.get('delay')

            my_tz = timezone('Europe/Berlin')

            send_mail_task.apply_async(([email], subject, text),
                                       eta=my_tz.localize(datetime.now()) + timedelta(seconds=minute * 60))
            serializer.save()

    def perform_update(self, serializer):
        if serializer.is_valid():
            validatedData = serializer.validated_data
            email = validatedData.get('email')
            subject = "Reminder from DRFRocketLoop"
            text = validatedData.get('text')
            minute = validatedData.get('delay')

            my_tz = timezone('Europe/Berlin')

            send_mail_task.apply_async(([email], subject, text),
                                       eta=my_tz.localize(datetime.now()) + timedelta(seconds=minute * 60))
            serializer.save()

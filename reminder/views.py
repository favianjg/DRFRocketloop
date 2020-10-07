from rest_framework import viewsets
from rest_framework.decorators import action

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

    @action(detail=True, methods=['post', 'put'])
    def send_email(self, request, *args, **kwargs):
        serializer = ReminderSerializer(data=request.data)
        email = serializer.data['email']
        text = serializer.data['text']
        # delay = serializer.data['delay']

        send_mail_task.apply_async(["rafcath95@gmail.com", ], "1234test123test", "test123body", countdown=1 * 60)

from reminder.models import Reminders
from reminder.serializers import ReminderSerializer
from rest_framework import generics

# Create your views here.
class ReminderList(generics.ListCreateAPIView):
    """
    List all reminders, or create a new reminder.
    """
    queryset = Reminders.objects.all()
    serializer_class = ReminderSerializer

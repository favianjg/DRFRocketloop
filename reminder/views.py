from rest_framework import generics

from reminder.models import Reminders
from reminder.serializers import ReminderSerializer, ReminderDetailSerializer


# Create your views here.
class ReminderList(generics.ListCreateAPIView):
    """
    List all reminders, or create a new reminder.
    """
    queryset = Reminders.objects.all()
    serializer_class = ReminderSerializer

class ReminderDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    List all reminders details, can update delay here
    """
    queryset = Reminders.objects.all()
    serializer_class = ReminderDetailSerializer

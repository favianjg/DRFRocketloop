from rest_framework import serializers

from reminder.models import Reminders


class ReminderSerializer(serializers.ModelSerializer):
   class Meta:
        model = Reminders
        fields = ['id', 'email', 'text', 'delay']

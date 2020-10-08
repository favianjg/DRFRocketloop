from rest_framework import serializers

from reminder.models import Reminders


class ReminderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Reminders
        fields = ['url', 'id', 'email', 'text', 'delay']

from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from reminder.views import ReminderViewSet

reminder_list = ReminderViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

reminder_detail = ReminderViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

urlpatterns = [
    path('reminders/', reminder_list, name='reminderlist'),
    path('reminders/<int:pk>/', reminder_detail, name='reminderdetail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)

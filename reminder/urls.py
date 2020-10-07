from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from reminder import views

urlpatterns = [
    path('reminders/', views.ReminderList.as_view()),
    path('reminders/<int:pk>/', views.ReminderDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
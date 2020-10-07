from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from boards import views

urlpatterns = [
    path('boards/', views.BoardList.as_view(), name='boardsoverview'),
    path('boardsdetail/', views.BoardDetailList.as_view(), name='boardslist'),
    path('boardsdetail/<int:pk>/', views.BoardDetail.as_view(), name='boardsdetail'),
    path('todos/', views.TodoList.as_view(), name='todoslist'),
    path('todos/<int:pk>/', views.TodoDetail.as_view(), name='todosdetail'),
    path('todosnotdone/', views.TodoNotDone.as_view(), name='todosnotdone')
]

urlpatterns = format_suffix_patterns(urlpatterns)
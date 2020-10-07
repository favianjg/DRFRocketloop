from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from boards import views

urlpatterns = [
    path('boards/', views.BoardList.as_view()),
    path('boardsdetail/', views.BoardDetailList.as_view()),
    path('boardsdetail/<int:pk>/', views.BoardDetail.as_view()),
    path('todos/', views.TodoList.as_view()),
    path('todos/<int:pk>/', views.TodoDetail.as_view()),
    path('todosnotdone/', views.TodoNotDone.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)
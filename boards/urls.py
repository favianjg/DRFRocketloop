from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from boards import views

board_view = views.BoardViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

board_detail = views.BoardDetailViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

todo_list = views.TodoViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

todo_detail = views.TodoViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

todo_notdone = views.TodoNotDoneViewSet.as_view({
    'get': 'list'
})

urlpatterns = [
    path('boards/', board_view, name='boardsoverview'),
    path('boardsdetail/<int:pk>/', board_detail, name='boardsdetail'),
    path('todos/', todo_list, name='todoslist'),
    path('todos/<int:pk>/', todo_detail, name='todosdetail'),
    path('todosnotdone/', todo_notdone, name='todosnotdone')
]

urlpatterns = format_suffix_patterns(urlpatterns)

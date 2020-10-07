from boards.models import Boards, Todos
from boards.serializers import BoardSerializer, BoardDetailSerializer, TodoSerializer
from rest_framework import generics

# Create your views here.
class BoardList(generics.ListAPIView):
    """
    List all boards with the todo_count field.
    """
    queryset = Boards.objects.all()
    serializer_class = BoardSerializer


class BoardDetailList(generics.ListCreateAPIView):
    """
    List all boards, or create a new board. Boards serialize all Todos
    """
    queryset = Boards.objects.all()
    serializer_class = BoardDetailSerializer

class BoardDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a board instance.
    """
    queryset = Boards.objects.all()
    serializer_class = BoardDetailSerializer

class TodoList(generics.ListCreateAPIView):
    """
    List all todos, or create a new todos.
    """
    queryset = Todos.objects.all()
    serializer_class = TodoSerializer

class TodoDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a todos instance.
    """
    queryset = Todos.objects.all()
    serializer_class = TodoSerializer

class TodoNotDone(generics.ListAPIView):
    """
    Filter all Todos that has the done flag set to false
    """
    serializer_class = TodoSerializer

    def get_queryset(self):
        status = False
        return Todos.objects.filter(done=status)

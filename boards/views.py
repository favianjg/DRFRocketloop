from boards.models import Boards, Todos
from boards.serializers import BoardSerializer, TodoSerializer
from rest_framework import generics

# Create your views here.
class BoardList(generics.ListCreateAPIView):
    """
    List all snippets, or create a new snippet.
    """
    queryset = Boards.objects.all()
    serializer_class = BoardSerializer

class BoardDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    queryset = Boards.objects.all()
    serializer_class = BoardSerializer

class TodoList(generics.ListCreateAPIView):
    """
    List all snippets, or create a new snippet.
    """
    queryset = Todos.objects.all()
    serializer_class = TodoSerializer

class TodoDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    queryset = Todos.objects.all()
    serializer_class = TodoSerializer

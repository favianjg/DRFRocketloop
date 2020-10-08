from datetime import datetime

from rest_framework import viewsets, mixins

from boards.models import Boards, Todos
from boards.serializers import BoardSerializer, BoardDetailSerializer, TodoSerializer


# Create your views here.
class BoardViewSet(mixins.ListModelMixin,
                   mixins.CreateModelMixin,
                   viewsets.GenericViewSet):
    """
    List all boards with the todo_count field.
    """
    queryset = Boards.objects.all()
    serializer_class = BoardSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class BoardDetailViewSet(mixins.RetrieveModelMixin,
                         mixins.UpdateModelMixin,
                         mixins.DestroyModelMixin,
                         viewsets.GenericViewSet):
    """
    List boards detail with todos listed
    """
    queryset = Boards.objects.all()
    serializer_class = BoardDetailSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class TodoViewSet(viewsets.ModelViewSet):
    """
    List all todos, or create a new todos.
    """
    queryset = Todos.objects.all()
    serializer_class = TodoSerializer

    def perform_update(self, serializer):
        if serializer.is_valid():
            serializer.validated_data['updated'] = datetime.now()
            serializer.save()


class TodoNotDoneViewSet(viewsets.ModelViewSet):
    """
    Filter all Todos that has the done flag set to false
    """
    serializer_class = TodoSerializer

    def get_queryset(self):
        status = False
        return Todos.objects.filter(done=status)

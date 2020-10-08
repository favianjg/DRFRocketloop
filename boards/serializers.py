from rest_framework import serializers

from boards.models import Boards, Todos


class BoardSerializer(serializers.HyperlinkedModelSerializer):
    todos_count = serializers.SerializerMethodField()

    def get_todos_count(self, obj):
        return len(obj.todos.all())

    class Meta:
        model = Boards
        fields = ['url', 'id', 'name', 'todos_count']

class BoardDetailSerializer(serializers.HyperlinkedModelSerializer):
    todos = serializers.HyperlinkedRelatedField(many=True, view_name='todosdetail', read_only=True)

    class Meta:
        model = Boards
        fields = ['url', 'id', 'name', 'todos']


class TodoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Todos
        fields = ['url', 'id', 'created', 'updated', 'title', 'done', 'board']

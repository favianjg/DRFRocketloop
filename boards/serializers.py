from rest_framework import serializers
from boards.models import Boards, Todos

class BoardSerializer(serializers.ModelSerializer):
   todos_count = serializers.SerializerMethodField()

   def get_todos_count(self, obj):
       return len(obj.todos.all())

   class Meta:
        model = Boards
        fields = ['id', 'name', 'todos_count']

class BoardDetailSerializer(serializers.ModelSerializer):
   class Meta:
        model = Boards
        fields = ['id', 'name', 'todos']

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todos
        fields = ['id', 'created', 'updated', 'title', 'done', 'board']
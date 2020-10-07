from rest_framework import serializers
from boards.models import Boards, Todos


class BoardSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=False, allow_blank=True, max_length=100)
    todos = serializers.PrimaryKeyRelatedField(many=True, queryset=Todos.objects.all(), allow_null=True)

    class Meta:
        model = Boards
        fields = ['id', 'name', 'todos']

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Boards.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.name = validated_data.get('title', instance.name)
        instance.save()
        return instance

class TodoSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=False, allow_blank=True, max_length=100)
    done = serializers.BooleanField(required=False)
    board = serializers.ReadOnlyField(source='board.id')

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Todos.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.title = validated_data.get('title', instance.title)
        instance.done = validated_data.get('done', instance.done)
        instance.save()
        return instance
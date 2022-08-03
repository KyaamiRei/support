from rest_framework import serializers

from .models import Comment, MessageRequest


class CommentSerializer(serializers.ModelSerializer):
    # класс сириаризатора для коментарий к тикету
    user = serializers.SlugRelatedField(slug_field="username", read_only=True)

    class Meta:
        model = Comment
        fields = "__all__"


class MessageSerializer(serializers.ModelSerializer):
    # сериализатор для просмотра списка тикетов
    user = serializers.SlugRelatedField(slug_field="username", read_only=True)
    comment = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = MessageRequest
        fields = "__all__"


class MessageCreateSerializer(serializers.ModelSerializer):
    # сериализатор для создание тикета
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = MessageRequest
        exclude = ("state", )


class CommentCreateSerializer(serializers.ModelSerializer):
    # сериализатор для создание комментарий
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Comment
        fields = "__all__"

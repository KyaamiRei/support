from rest_framework import serializers

from .models import MessageRequest


# создние класса сириаризатора
class MessageSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = MessageRequest
        fields = ('user', 'title', 'content', 'created_at', 'state')

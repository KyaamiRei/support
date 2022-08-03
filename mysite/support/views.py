from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet


from .models import MessageRequest
from .permissions import IsAdminOrReadOnly
from .serializers import (
    CommentCreateSerializer,
    MessageCreateSerializer,
    MessageSerializer,
)


# преставление для просмотра тикетов, редактирование доступно только администратору
class MessageViewSet(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    mixins.ListModelMixin,
    GenericViewSet,
):
    queryset = MessageRequest.objects.all()
    serializer_class = MessageSerializer
    permission_classes = (IsAdminOrReadOnly, )


# представление для создания тикета, только для авторизированных пользователей
class MessageCreateViewSet(
    mixins.CreateModelMixin,
    GenericViewSet,
):
    serializer_class = MessageCreateSerializer
    permission_classes = (IsAuthenticated, )
    


# предсьтавление для создания комментарий к тикету
class CommentCreateViewSet(
    mixins.CreateModelMixin,
    GenericViewSet,
):
    serializer_class = CommentCreateSerializer
    permission_classes = (IsAuthenticated, )

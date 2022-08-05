from rest_framework import routers

from .views import (
    CommentCreateViewSet,
    MessageViewSet,
)


# сохдание объекта роутера и его регистрация на основе созданного ViewSet
router = routers.DefaultRouter()
router.register(r'message', MessageViewSet)
router.register(r'comment', CommentCreateViewSet)

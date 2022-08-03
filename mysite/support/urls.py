from django.urls import include, path

from rest_framework import routers

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

# from .router import router

from .views import (
    CommentCreateViewSet,
    MessageCreateViewSet,
    MessageViewSet,
)


# сохдание объекта роутера и его регистрация на основе созданного ViewSet
router = routers.DefaultRouter()
router.register(r'message', MessageViewSet)
# router.register(r'comment', CommentCreateViewSet)


urlpatterns = [
    # набор ввсех маршрутов в наборе router
    path('', include(router.urls)),
    # создание тикета
    path('messagecreate/', MessageCreateViewSet.as_view({'post': 'create'})),
    # создание комментария
    path('comment/', CommentCreateViewSet.as_view({'post': 'create'})),
    # простая авторизация
    path('app-auth/', include('rest_framework.urls')),
    # JWT авторизация
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]

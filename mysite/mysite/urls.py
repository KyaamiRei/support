from django.contrib import admin
from django.urls import include, path, re_path

from rest_framework import routers

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

# , MessageViewSet
from support.views import MessageAPIDestroy, MessageAPIList, MessageAPIUpdate


urlpatterns = [
    path('admin/', admin.site.urls),
    # набор ввсех маршрутов в наборе router
    # path('api/v1/', include(router.urls)),
    path('api/message/', MessageAPIList.as_view()),
    path('api/message/<int:pk>/', MessageAPIUpdate.as_view()),
    path('api/messagedelete/<int:pk>/', MessageAPIDestroy.as_view()),
    # простая авторизация 
    path('api/app-auth', include('rest_framework.urls')),
    # авторизация через токен
    path(r'^auth/', include('djoser.urls')),
    # JWT авторизация 
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]

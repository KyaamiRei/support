from django.contrib import admin
from django.urls import path

from support.views import MessageAPIList, MessageAPIUpdate, MessageDetailAPIView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/messagelist/', MessageAPIList.as_view()),
    path('api/v1/messagelist/<int:pk>/', MessageAPIUpdate.as_view()),
    path('api/v1/messagedetail/<int:pk>/', MessageDetailAPIView.as_view()),
]

from django.contrib import admin

from .models import Comment, MessageRequest


# Регистрация моделей для админпанели
admin.site.register(MessageRequest)
admin.site.register(Comment)

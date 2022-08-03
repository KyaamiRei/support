from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class MessageRequest(models.Model):
    # создание модели тикета
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    user_email = models.EmailField(max_length=254, verbose_name='Электронная почта')
    title = models.CharField(max_length=150, verbose_name='Тема заявки')
    content = models.TextField(blank=True, verbose_name='Описание проблемы')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    STATE_MESSAGE = [
        ('Act', 'Выполняется'),
        ('Stp', 'Отложена'),
        ('Cmp', 'Завершена'),
    ]
    # состояние заявки
    state = models.CharField(max_length=3, choices=STATE_MESSAGE, default='R', verbose_name='Состояние заявки')

    def get_absolute_url(self):
        return reverse('view_request', kwargs={'pk': self.pk})

    # возвращает вместо объекта при вызове указанное поле title, а не поле с индексом
    def __str__(self):
        return self.title

    # мета класс для переименонвания модели в админ панели
    class Meta:
        verbose_name = 'Тикет'
        verbose_name_plural = 'Тикеты'
        ordering = ['-created_at']


# модель комментариq, при помощи которой сапорт может ответить на тикет пользователя
class Comment(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    content = models.TextField(blank=True, verbose_name='Контент')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    message_req = models.ForeignKey(
        MessageRequest, on_delete=models.CASCADE,
        verbose_name='Заявка', related_name="comment",
    )

    def __str__(self):
        return f'{self.user}'

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
        ordering = ['created_at']

from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


# создание моделей
class MessageRequest(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.PROTECT)
    # наименование заявки
    title = models.CharField(max_length=150, verbose_name='Тема заявки')
    # Описание проблемы для СП
    content = models.TextField(blank=True, verbose_name='Описание проблемы')
    # Дата публикации заявки
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    STATE_MESSAGE = [
        ('R', 'Выполняется'),
        ('S', 'Отложена'),
        ('F', 'Завершена'),
    ]
    # состояние заявки
    state = models.CharField(max_length=1, choices=STATE_MESSAGE, default='R', verbose_name='Состояние заявки')

    def get_absolute_url(self):
        return reverse('view_request', kwargs={'pk': self.pk})

    # возвращает вместо объекта при вызове указанное поле title, а не поле с индексом
    def __str__(self):
        return self.title

    # мета класс для переименонвания модели в админ панели
    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'
        ordering = ['-created_at']


# модель комментарий
class Comment(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.PROTECT)
    message_req = models.ForeignKey(MessageRequest, on_delete=models.PROTECT, verbose_name='Заявка', null=True)
    # ответ специалиста или же дополнение проблемы от пользователя
    content = models.TextField(blank=True, verbose_name='Контент')
    # Дата пуликакции
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')

    def get_absolute_url(self):
        return reverse('comment', kwargs={'pk': self.pk})

    def __str__(self):
        return self.content

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
        ordering = ['-created_at']

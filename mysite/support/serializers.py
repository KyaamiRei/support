# import io

from rest_framework import serializers
# from rest_framework.parsers import JSONParser
# from rest_framework.renderers import JSONRenderer

from .models import MessageRequest


# class SupportModel:
#     def __init__(self, user_id, title, content):
#         self.user_id = user_id
#         self.title = title
#         self.content = content


# создние класса сириаризатора
class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = MessageRequest
        fields = ('user', 'title', 'content', 'created_at', 'state')


# преобразование модели заявки в json формат
# def encode():
#     model = SupportModel(1, 'Problem #4', 'Content problem')
#     model_sr = MessageSerializer(model)
#     print(model_sr.data, type(model_sr.data), sep='\n')
#     json = JSONRenderer().render(model_sr.data)
#     print(json)


# # преобразование json объекта в объект python
# def decode():
#     stream = io.BytesIO(b'{"user_id": "1", "title": "Problem #5", "content": "Content problem 5"}')
#     data = JSONParser().parse(stream)
#     serilizer = MessageSerializer(data=data)
#     serilizer.is_valid()
#     print(serilizer.validated_data)

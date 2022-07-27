from django.forms import model_to_dict

from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from django.shortcuts import render

from .models import MessageRequest
from .serializers import MessageSerializer


class MessageAPIList(generics.ListCreateAPIView):
    queryset = MessageRequest.objects.all()
    serializer_class = MessageSerializer


class MessageAPIUpdate(generics.UpdateAPIView):
    queryset = MessageRequest.objects.all()
    serializer_class = MessageSerializer


class MessageDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MessageRequest.objects.all()
    serializer_class = MessageSerializer


# class MessageAPIView(APIView):
#     def get(self, request):
#         message_list = MessageRequest.objects.all()
#         return Response({'posts': MessageSerializer(message_list, many=True).data})

#     def post(self, request):
#         serializer = MessageSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()

#         return Response({'post': serializer.data})

#     def put(self, request, **kwargs):
#         pk = kwargs.get("pk", None)
#         if not pk:
#             return Response({"error": "Method PUT not allowed"})

#         try:
#             instance = MessageRequest.objects.get(pk=pk)
#         except:
#             return Response({"error": "Object does non exists"})

#         serializer = MessageSerializer(data=request.data, instance=instance)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({"post": serializer.data})

#     def delete(self, request, **kwargs):
#         pk = kwargs.get("pk", None)
#         if not pk:
#             return Response({"error": "Method DELETE not allowed"})

#         try:
#             instance = MessageRequest.objects.get(pk=pk)
#         except:
#             return Response({"error": "Object does non exists"})

#         serializer = MessageSerializer(data=request.data, instance=instance)
#         serializer.is_valid(raise_exception=True)

#         return Response({"post": "Deleted post" + str(pk)})


# создание своего представления для модели
# class MessageAPIView(generics.ListAPIView):
#     queryset = MessageRequest.objects.all()
#     serializer_class = MessageSerializer

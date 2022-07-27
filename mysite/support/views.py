from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAdminUser, IsAuthenticated, IsAuthenticatedOrReadOnly

from .models import Comment, MessageRequest
from .permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly
from .serializers import MessageSerializer


class MessageAPIListPagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = 'page_size'
    max_page_size = 5


class MessageAPIList(generics.ListCreateAPIView):
    queryset = MessageRequest.objects.all()
    serializer_class = MessageSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )
    pagination_class = MessageAPIListPagination


class MessageAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = MessageRequest.objects.all()
    serializer_class = MessageSerializer
    permission_classes = (IsAuthenticated, )
    # authentication_classes = (TokenAuthentication, )


class MessageAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = MessageRequest.objects.all()
    serializer_class = MessageSerializer
    permission_classes = (IsAdminOrReadOnly, )


# class MessageViewSet(viewsets.ModelViewSet):
#     # queryset = MessageRequest.objects.all()
#     serializer_class = MessageSerializer

#     def get_queryset(self):
#         pk = self.kwargs.get("pk")

#         if not pk:
#             MessageRequest.objects.all()[:3]

#         return MessageRequest.objects.filter(pk=pk)

#     @action(methods=['get'], detail=True)
#     def comment(self, request, pk=None):
#         comments = Comment.objects.get(pk=pk)
#         return Response({'comment': comments.content})

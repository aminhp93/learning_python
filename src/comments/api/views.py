from rest_framework.generics import (
		ListAPIView,
		CreateAPIView,
		RetrieveAPIView
	)

from comments.models import Comment
from .serializers import CommentListSerializer, CommentDetailSerializer

class CommentListAPIView(ListAPIView):
	serializer_class = CommentListSerializer

	def get_queryset(self):
		queryset_list = Comment.objects.all()
		return queryset_list

class CommentDetailAPIView(RetrieveAPIView):
	serializer_class = CommentDetailSerializer

	def get_queryset(self):
		queryset_list = Comment.objects.filter(id__gte=0)
		return queryset_list
		
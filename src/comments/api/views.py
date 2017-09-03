from rest_framework.generics import (
		ListAPIView,
		CreateAPIView,
		RetrieveAPIView
	)

from posts.api.pagination import PostPageNumberPagination
from comments.models import Comment
from .serializers import CommentListSerializer, CommentDetailSerializer

class CommentListAPIView(ListAPIView):
	serializer_class = CommentListSerializer
	pagination_class = PostPageNumberPagination

	def get_queryset(self):
		queryset_list = Comment.objects.all()
		return queryset_list

	def finalize_response(self, request, response, *args, **kwargs):
		response.data['status_code'] = response.status_code
		return super(CommentListAPIView, self).finalize_response(request, response, *args, **kwargs)

class CommentDetailAPIView(RetrieveAPIView):
	serializer_class = CommentDetailSerializer
	pagination_class = PostPageNumberPagination

	def finalize_response(self, request, response, *args, **kwargs):
		response.data['status_code'] = response.status_code
		return super(CommentListAPIView, self).finalize_response(request, response, *args, **kwargs)

	def get_queryset(self):
		queryset_list = Comment.objects.filter(id__gte=0)
		return queryset_list
		
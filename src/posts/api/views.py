from rest_framework.generics import (
		ListAPIView,
		CreateAPIView,
		RetrieveAPIView,
		RetrieveUpdateAPIView,
		DestroyAPIView,
	)

from rest_framework.renderers import JSONRenderer
from rest_framework import status
from rest_framework.response import Response
from rest_framework import renderers, generics

from posts.models import Post

from .pagination import (
		PostPageNumberPagination,
		PostLimitOffsetPagination
	)

from .permissions import IsOwnerOrReadOnly

from .serializers import (
		PostListSerializer,
		PostCreateUpdateSerializer,
		PostDetailSerializer,
	)

from rest_framework.permissions import (
		AllowAny,
		IsAuthenticated,
		IsAdminUser,
		IsAuthenticatedOrReadOnly,
	)

# from oauth2_provider.ext.rest_framework import TokenHasReadWriteScope, TokenHasScope

class PostListAPIView(ListAPIView):
	serializer_class = PostListSerializer
	pagination_class = PostPageNumberPagination
	permission_class = [IsAuthenticated,]

	def get_queryset(self, *args, **kwargs):
		queryset_list = Post.objects.all()
		return queryset_list

	def finalize_response(self, request, response, *args, **kwargs):
		response.data['status_code'] = response.status_code
		return super(PostListAPIView, self).finalize_response(request, response, *args, **kwargs)

class PostCreateAPIView(CreateAPIView):
	serializer_class = PostCreateUpdateSerializer

	def handle_exception(self, exc):
		print(exc.status_code)

		return super(PostCreateAPIView, self).handle_exception(exc)

	def finalize_response(self, request, response, *args, **kwargs):
		response.data['status_code'] = response.status_code
		return super(PostCreateAPIView, self).finalize_response(request, response, *args, **kwargs)

class PostDetailAPIView(RetrieveAPIView):
	pagination_class = PostPageNumberPagination
	serializer_class = PostDetailSerializer
	lookup_field = 'slug'

	def get_queryset(self, *args, **kwargs):
		queryset_list = Post.objects.all()
		return queryset_list

	def finalize_response(self, request, response, *args, **kwargs):
		response.data['status_code'] = response.status_code
		return super(PostDetailAPIView, self).finalize_response(request, response, *args, **kwargs)

class PostUpdateAPIView(RetrieveUpdateAPIView):
	serializer_class = PostCreateUpdateSerializer
	queryset = Post.objects.all()
	lookup_field = 'slug'

class PostDeleteAPIView(DestroyAPIView):
	serializer_class = PostDetailSerializer
	queryset = Post.objects.all()
	lookup_field = "slug"




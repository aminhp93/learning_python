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

from books.models import Book

from .pagination import (
		BookPageNumberPagination,
		BookLimitOffsetPagination
	)

from .permissions import IsOwnerOrReadOnly

from .serializers import (
		BookListSerializer,
		BookCreateUpdateSerializer,
		BookDetailSerializer,
	)

from rest_framework.permissions import (
		AllowAny,
		IsAuthenticated,
		IsAdminUser,
		IsAuthenticatedOrReadOnly,
	)

# from oauth2_provider.ext.rest_framework import TokenHasReadWriteScope, TokenHasScope

class BookListAPIView(ListAPIView):
	serializer_class = BookListSerializer
	pagination_class = BookPageNumberPagination
	permission_class = [IsAuthenticated,]

	def get_queryset(self, *args, **kwargs):
		queryset_list = Book.objects.all()
		return queryset_list

	def list(self, request, *args, **kwargs):
		queryset = self.filter_queryset(self.get_queryset())

		page = self.paginate_queryset(queryset)
		if page is not None:
			serializer = self.get_serializer(page, many=True)
			return self.get_paginated_response(serializer.data)

		serializer = self.get_serializer(queryset, many=True)

		return Response(serializer.data)

class BookCreateAPIView(CreateAPIView):
	serializer_class = BookCreateUpdateSerializer

class BookDetailAPIView(RetrieveAPIView):
	serializer_class = BookDetailSerializer
	lookup_field = 'slug'

	def get_queryset(self, *args, **kwargs):
		queryset_list = Book.objects.all()
		return queryset_list

class BookUpdateAPIView(RetrieveUpdateAPIView):
	serializer_class = BookCreateUpdateSerializer
	queryset = Book.objects.all()
	lookup_field = 'slug'

class BookDeleteAPIView(DestroyAPIView):
	serializer_class = BookDetailSerializer
	queryset = Book.objects.all()
	lookup_field = "slug"






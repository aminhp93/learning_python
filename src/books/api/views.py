from rest_framework.generics import (
		ListAPIView,
		CreateAPIView,
		RetrieveAPIView,
		RetrieveUpdateAPIView,
		DestroyAPIView,
	)

from books.models import Book

from .serializers import (
		BookListSerializer,
		BookCreateUpdateSerializer,
		BookDetailSerializer,
	)

class BookListAPIView(ListAPIView):
	serializer_class = BookListSerializer

	def get_queryset(self, *args, **kwargs):
		queryset_list = Book.objects.all()
		return queryset_list

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






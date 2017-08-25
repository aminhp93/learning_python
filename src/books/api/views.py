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

	def dispatch(self, request, *args, **kwargs):
		"""
		`.dispatch()` is pretty much the same as Django's regular dispatch,
		but with extra hooks for startup, finalize, and exception handling.
		"""
		self.args = args
		self.kwargs = kwargs
		request = self.initialize_request(request, *args, **kwargs)
		self.request = request
		self.headers = self.default_response_headers  # deprecate?

		try:
			self.initial(request, *args, **kwargs)

			# Get the appropriate handler method
			if request.method.lower() in self.http_method_names:
				handler = getattr(self, request.method.lower(),
								  self.http_method_not_allowed)
			else:
				handler = self.http_method_not_allowed

			response = handler(request, *args, **kwargs)

		except Exception as exc:
			response = self.handle_exception(exc)

		self.response = self.finalize_response(request, response, *args, **kwargs)
		response.data['status_code'] = response.status_code
		return response

class BookCreateAPIView(CreateAPIView):
	serializer_class = BookCreateUpdateSerializer

class BookDetailAPIView(RetrieveAPIView):
	serializer_class = BookDetailSerializer
	lookup_field = 'slug'

	def get_queryset(self, *args, **kwargs):
		queryset_list = Book.objects.all()
		return queryset_list

	def dispatch(self, request, *args, **kwargs):
		"""
		`.dispatch()` is pretty much the same as Django's regular dispatch,
		but with extra hooks for startup, finalize, and exception handling.
		"""
		self.args = args
		self.kwargs = kwargs
		request = self.initialize_request(request, *args, **kwargs)
		self.request = request
		self.headers = self.default_response_headers  # deprecate?

		try:
			self.initial(request, *args, **kwargs)

			# Get the appropriate handler method
			if request.method.lower() in self.http_method_names:
				handler = getattr(self, request.method.lower(),
								  self.http_method_not_allowed)
			else:
				handler = self.http_method_not_allowed

			response = handler(request, *args, **kwargs)

		except Exception as exc:
			response = self.handle_exception(exc)

		self.response = self.finalize_response(request, response, *args, **kwargs)
		response.data['status_code'] = response.status_code
		return response

class BookUpdateAPIView(RetrieveUpdateAPIView):
	serializer_class = BookCreateUpdateSerializer
	queryset = Book.objects.all()
	lookup_field = 'slug'

class BookDeleteAPIView(DestroyAPIView):
	serializer_class = BookDetailSerializer
	queryset = Book.objects.all()
	lookup_field = "slug"


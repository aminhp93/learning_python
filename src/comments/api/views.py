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
		print(type(response.data))
		print(response.status_code)
		response.data[-1] = {'status': response.status_code}
		return response

class CommentDetailAPIView(RetrieveAPIView):
	serializer_class = CommentDetailSerializer

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

	def get_queryset(self):
		queryset_list = Comment.objects.filter(id__gte=0)
		return queryset_list
		
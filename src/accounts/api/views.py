from rest_framework.generics import (
		ListAPIView,
		CreateAPIView,
		RetrieveAPIView
	)

from posts.api.pagination import PostPageNumberPagination
from accounts.models import MyUser
from .serializers import UserListSerializer, UserDetailSerializer

class UserListAPIView(ListAPIView):
	serializer_class = UserListSerializer
	pagination_class = PostPageNumberPagination

	def get_queryset(self):

		queryset_list = MyUser.objects.all()
		print(queryset_list)
		return queryset_list

	def finalize_response(self, request, response, *args, **kwargs):
		response.data['status_code'] = response.status_code
		return super(UserListAPIView, self).finalize_response(request, response, *args, **kwargs)

class UserDetailAPIView(RetrieveAPIView):
	serializer_class = UserDetailSerializer
	pagination_class = PostPageNumberPagination

	def finalize_response(self, request, response, *args, **kwargs):
		response.data['status_code'] = response.status_code
		return super(UserDetailAPIView, self).finalize_response(request, response, *args, **kwargs)

	def get_queryset(self):
		queryset_list = MyUser.objects.filter(id__gte=0)
		return queryset_list
		
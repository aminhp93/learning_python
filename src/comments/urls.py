from django.conf.urls import url
from .views import (
		# CommentCreateView,
		CommentDetailView,
		CommentDeleteView,
		# CommentListView,
		# CommentUpdateView,
	)

urlpatterns = [
	# url(r'^$', CommentListView.as_view(), name='list'),
	# url(r'^create/$', CommentCreateView.as_view(), name='create'),
	url(r'^(?P<id>\d+)/$', CommentDetailView.as_view(), name='detail'),
	# url(r'^(?P<id>\d+)/update/$', CommentUpdateView.as_view(), name='update'),
	url(r'^(?P<id>\d+)/delete/$', CommentDeleteView.as_view(), name='delete')
]
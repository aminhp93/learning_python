from django.conf.urls import url

from .views import (
		BookListAPIView,
		BookCreateAPIView,
		BookDetailAPIView,
		BookUpdateAPIView,
		BookDeleteAPIView,
	)

urlpatterns = [
	url(r'^$', BookListAPIView.as_view(), name='list'),
	url(r'^create/$', BookCreateAPIView.as_view(), name='create'),
	url(r'^(?P<slug>[\w-]+)/$', BookDetailAPIView.as_view(), name='detail'),
	url(r'^(?P<slug>[\w-]+)/update/$', BookUpdateAPIView.as_view(), name='update'),
	url(r'^(?P<slug>[\w-]+)/delete/$', BookDeleteAPIView.as_view(), name='delete'),
]
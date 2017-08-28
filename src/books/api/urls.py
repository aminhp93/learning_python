from django.conf.urls import url

from books.api import views

urlpatterns = [
	url(r'^$', views.BookListAPIView.as_view(), name='list'),
	url(r'^create/$', views.BookCreateAPIView.as_view(), name='create'),
	url(r'^(?P<slug>[\w-]+)/$', views.BookDetailAPIView.as_view(), name='detail'),
	url(r'^(?P<slug>[\w-]+)/update/$', views.BookUpdateAPIView.as_view(), name='update'),
	url(r'^(?P<slug>[\w-]+)/delete/$', views.BookDeleteAPIView.as_view(), name='delete'),
]
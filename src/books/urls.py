from django.conf.urls import url
from .views import (
        BookListView,
        BookCreateView,
        # BookDetailView,
        book_detail,
        BookUpdateView,
        BookDeleteView,
    )

urlpatterns = [
    url(r'^$', BookListView.as_view(), name='list'),
    url(r'^create/$', BookCreateView.as_view(), name='create'),
    url(r'^(?P<slug>[-\w]+)/$', book_detail, name='detail'),
    # url(r'^(?P<slug>[-\w]+)/$', BookDetailView.as_view(), name='detail'),
    url(r'^(?P<slug>[-\w]+)/update/$', BookUpdateView.as_view(), name='update'),
    url(r'^(?P<slug>[-\w]+)/delete/$', BookDeleteView.as_view(), name='delete'),

]

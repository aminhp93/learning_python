from django.conf.urls import url
from .views import (
        PostListView,
        PostCreateView,
        PostDetailView,
        PostUpdateView,
        PostDeleteView,
    )

urlpatterns = [
    url(r'^$', PostListView.as_view(), name='list'),
    url(r'^create/$', PostCreateView.as_view(), name='create'),
    url(r'^(?P<slug>[-\w]+)/$', PostDetailView.as_view(), name='detail'),
    url(r'^(?P<slug>[-\w]+)/update/$', PostUpdateView.as_view(), name='update'),
    url(r'^(?P<slug>[-\w]+)/delete/$', PostDeleteView.as_view(), name='delete'),

]

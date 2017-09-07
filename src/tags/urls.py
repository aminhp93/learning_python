
from django.conf.urls import url
from .views import tag_list, tag_related

urlpatterns = [
	url(r'^$', tag_list, name='list'),
	url(r'^(?P<slug>[\w-]+)/$', tag_related, name='related'),
]
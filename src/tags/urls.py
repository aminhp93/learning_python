from django.urls import url

urlpatterns = [
	url(r'^$', tag_list, name='list'),
	url(r'^(?P<slug>[\w-]+)/$', tag_detail, name='detail'),
]
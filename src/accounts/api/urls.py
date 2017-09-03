from django.conf.urls import url

from accounts.api import views

urlpatterns = [
	url(r'^$', views.UserListAPIView.as_view(), name='list'),
	# url(r'^create/$', views.UserCreateAPIView.as_view(), name='create'),
	url(r'^(?P<pk>\d+)/$', views.UserDetailAPIView.as_view(), name='detail'),
	# url(r'^(?P<slug>[\w-]+)/update/$', views.UserUpdateAPIView.as_view(), name='update'),
	# url(r'^(?P<slug>[\w-]+)/delete/$', views.UserDeleteAPIView.as_view(), name='delete'),
]
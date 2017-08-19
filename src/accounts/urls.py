from django.conf.urls import url

from .views import (login_view, register_view, logout_view, confirm_email)

urlpatterns = [
	url(r'^confirm_email/(?P<token>[\w.-]+)/$', confirm_email, name='confirm_email'),
	url(r'^register/$', register_view, name='register'),
    url(r'^login/$', login_view, name='login'),
    url(r'^logout/$', logout_view, name='logout'),
]
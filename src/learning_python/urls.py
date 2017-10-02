"""learning_python URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from django.conf.urls.i18n import i18n_patterns

from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Pastebin API')

from .views import Home, Contact, RootAPIView, translate

from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token

urlpatterns = [
    url(r'^i18n/', include('django.conf.urls.i18n')),
    url(r'^admin/', admin.site.urls),
    url(r'^$', Home.as_view(), name='home'),
    url(r'^contact/$', Contact.as_view(), name='contact'),
    url(r'^accounts/', include('accounts.urls', namespace='accounts')),
    url(r'^comments/', include('comments.urls', namespace='comments')),
    url(r'^posts/', include('posts.urls', namespace='posts')),
    url(r'^tags/', include('tags.urls', namespace='tags')),
    url(r'^oauth/', include('social_django.urls', namespace='social')),  # <--
    url(r'^search/', include('haystack.urls')),

    # =========================== API ====================================
    url(r'^api-token-auth/', obtain_jwt_token),
    url(r'^api-token-refresh/', refresh_jwt_token),
    url(r'^api-token-verify/', verify_jwt_token),
    url(r'^api/$', RootAPIView.as_view(), name='root-api'),
    url(r'^api/users/', include('accounts.api.urls', namespace='users-api')),
    url(r'^api/posts/', include('posts.api.urls', namespace='posts-api')),
    url(r'^api/comments/', include('comments.api.urls', namespace='comments-api')),  
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^swagger/$', schema_view), 
    url(r'^markdownx/', include('markdownx.urls')),

]

urlpatterns += i18n_patterns(
    url(r'^translate/$', translate, name='translate'),
)

# Django Resframework Authentication



handler400 = 'learning_python.views.error400'
handler403 = 'learning_python.views.error403'
handler404 = 'learning_python.views.error404'
handler500 = 'learning_python.views.error500'

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


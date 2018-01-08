from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from django.conf.urls.i18n import i18n_patterns

from .views import Home, Contact, RootAPIView, translate, autocomplete

urlpatterns = [
    url(r'^i18n/', include('django.conf.urls.i18n')),
    url(r'^admin/', admin.site.urls),
    url(r'^$', Home.as_view(), name='home'),
    url(r'^contact/$', Contact.as_view(), name='contact'),
    url(r'^accounts/', include('accounts.urls', namespace='accounts')),
    url(r'^comments/', include('comments.urls', namespace='comments')),
    url(r'^posts/', include('posts.urls', namespace='posts')),
    url(r'^tags/', include('tags.urls', namespace='tags')),
    url(r'^oauth/', include('social_django.urls', namespace='social')),
    url(r'^search/', include('haystack.urls')),
    url(r'^search/autocomplete/$', autocomplete),

    # =========================== API ====================================

    url(r'^api/$', RootAPIView.as_view(), name='root-api'),
    url(r'^api/users/', include('accounts.api.urls', namespace='users-api')),
    url(r'^api/posts/', include('posts.api.urls', namespace='posts-api')),
    url(r'^api/comments/', include('comments.api.urls', namespace='comments-api')),  
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^markdownx/', include('markdownx.urls')),
]

urlpatterns += i18n_patterns(
    url(r'^translate/$', translate, name='translate'),
)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


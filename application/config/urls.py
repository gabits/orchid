from django.conf.urls import url, include
from django.conf import settings
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^', include('dashboard.urls')),
    url(r'^gallery', include('gallery.urls')),
    url(r'^articles', include('articles.urls')),
]


if settings.DEBUG:
    # Serve staticfiles locally
    urlpatterns += staticfiles_urlpatterns()
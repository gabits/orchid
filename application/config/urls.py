from django.conf import settings

from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import reverse_lazy

from django.views.generic import RedirectView


urlpatterns = [
    # Django Admin
    url(r'^admin/', admin.site.urls),

    # Homepage redirection
    url(r'^$', RedirectView.as_view(url=reverse_lazy('dashboard:test')), name='home'),

    # Apps URLConfs
    url(r'^dashboard',
        include('dashboard.urls',
        namespace='dashboard')),

    url(r'^gallery',
        include('gallery.urls',
        namespace='gallery')),

    url(r'^articles',
        include('articles.urls',
        namespace='articles')),
]


if settings.DEBUG:
    # Serve staticfiles locally
    urlpatterns += staticfiles_urlpatterns()
from __future__ import unicode_literals

from django.conf.urls import include, url

from .views import WorksGalleryView


urlpatterns = [
    url(r'^gallery', WorksGalleryView.as_view())
]

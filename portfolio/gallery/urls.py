from __future__ import unicode_literals

from django.conf.urls import url

from .views import MainGalleryView


urlpatterns = [
    url(r'^$', MainGalleryView.as_view(), name='gallery'),
]

from __future__ import unicode_literals

from django.conf.urls import url

from .views import GalleriesListView


urlpatterns = [
    url(r'^$', GalleriesListView.as_view(), name='gallery'),
]

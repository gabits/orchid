from __future__ import unicode_literals

from django.conf.urls import url
from django.urls import reverse_lazy
from django.views.generic import RedirectView

from .views import MainGalleryView


urlpatterns = [
    url(r'^$', RedirectView.as_view(url=reverse_lazy('gallery'), permanent=False), name='home'),
    url(r'^gallery', MainGalleryView.as_view(), name='gallery'),
]

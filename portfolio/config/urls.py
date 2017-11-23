from django.conf.urls import url, include
from django.urls import reverse_lazy
from django.contrib import admin
from django.views.generic import RedirectView

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^$', RedirectView.as_view(url=reverse_lazy('gallery'), permanent=False), name='home'),
    url(r'^gallery/', include('gallery.urls')),
]

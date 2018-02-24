from django.conf.urls import url, include
from django.contrib import admin


urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^', include('dashboard.urls')),
    url(r'^gallery', include('gallery.urls')),
]
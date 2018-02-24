from django.views.generic import ListView

from .models.gallery import Gallery


class GalleriesListView(ListView):
    model = Gallery
    template_name = 'gallery_list.html'

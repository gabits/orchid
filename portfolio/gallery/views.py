from django.views.generic import ListView

from .models.gallery import Gallery


class MainGalleryView(ListView):
    model = Gallery
    template_name = 'works/gallery_list.html'

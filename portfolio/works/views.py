from django.views.generic import ListView

from .models.gallery import GallerySection


class MainGalleryView(ListView):
    model = GallerySection
    template_name = 'works/gallery_list.html'

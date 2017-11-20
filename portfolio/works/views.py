from django.views.generic import ListView

from works.models.media import Photograph
from .models.gallery import GallerySection


class MainGalleryView(ListView):
    model = GallerySection
    template_name = 'works/gallery_list.html'


class PhotographView(ListView):
    model = Photograph
    template_name = 'works/gallery_list.html'

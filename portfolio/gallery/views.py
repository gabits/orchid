from django.views.generic import ListView

from .models.gallery import Gallery


class MainGalleryView(ListView):
    model = Gallery
    template_name = 'gallery_list.html'

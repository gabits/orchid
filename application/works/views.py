from django.views.generic import ListView

from .models.media import Photograph


class PhotographView(ListView):
    model = Photograph
    template_name = 'works/gallery_list.html'

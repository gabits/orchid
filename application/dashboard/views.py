from django.urls import reverse_lazy
from django.views.generic import RedirectView


class DashboardTemplateView(RedirectView):
    """View for the first page users see when they visit the website.
    """

    def get_redirect_url(self, *args, **kwargs):
        return reverse_lazy('article_detail')

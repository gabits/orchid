from django.views.generic import TemplateView


class DashboardTemplateView(TemplateView):
    """View for the first page users see when they visit the website.
    """

    template_name = 'dashboard/base_dashboard.html'

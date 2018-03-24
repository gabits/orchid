from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$',
        views.DashboardTemplateView.as_view(),
        name='test'
        ),
]

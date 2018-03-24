from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$',
        views.ArticleListView.as_view(),
        name='article_detail'),

    url(r'new/',
        views.AddEditArticleView.as_view(),
        name='add_article'),

]

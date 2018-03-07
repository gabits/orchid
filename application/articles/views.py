from django.views.generic import ListView

from .models import Article


class ArticleListView(ListView):
    template_name = 'articles/article_detail.html'
    model = Article

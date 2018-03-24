from django.views import generic as django_views

from .forms import ArticleForm
from .models import Article


class ArticleListView(django_views.ListView):
    template_name = 'articles/article_list.html'
    model = Article
    queryset = Article.objects.all()
    ordering = ['-created_at']          # TODO: Replace this by published_at once implemented


class AddEditArticleView(django_views.FormView):
    template_name = 'articles/add_or_edit_article.html'
    model = Article
    form_class = ArticleForm

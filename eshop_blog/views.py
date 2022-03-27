from django.views import generic
from .models import Article


class ArticleList(generic.ListView):
    model = Article


class ArticleDetail(generic.DetailView):
    model = Article

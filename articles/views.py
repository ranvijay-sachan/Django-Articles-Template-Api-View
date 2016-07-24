import random

from django.views.generic import ListView, DetailView

from articles.models import Article


class ArticleList(ListView):
    model = Article
    template_name = 'articles.html'
    context_object_name = "articles"
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super(ArticleList, self).get_context_data(**kwargs)
        read_list = list(Article.objects.all())
        random.shuffle(read_list)
        context['read_more'] = read_list[:4]
        return context


class ArticleDetail(DetailView):
    model = Article
    template_name = 'article_detail.html'
    context_object_name = "article"

    def get_context_data(self, **kwargs):
        context = super(ArticleDetail, self).get_context_data(**kwargs)
        read_list = list(Article.objects.all())
        random.shuffle(read_list)
        context['read_more'] = read_list[:4]
        return context

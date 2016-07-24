from django.conf.urls import url
from articles.views import ArticleList, ArticleDetail

urlpatterns = [
    url(r'^articles/$', ArticleList.as_view(), name='article-list'),
    url(r'^article/(?P<pk>[0-9]+)/$', ArticleDetail.as_view(), name='article-detail'),
]
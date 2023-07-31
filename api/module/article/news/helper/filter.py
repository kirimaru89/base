from django_filters import rest_framework as filters

from module.article.news.models import News


class NewsFilter(filters.FilterSet):
    class Meta:
        model = News
        exclude = ()

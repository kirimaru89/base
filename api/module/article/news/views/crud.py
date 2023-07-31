from django.db import transaction
from django.shortcuts import get_object_or_404
from rest_framework.decorators import action
from rest_framework.viewsets import GenericViewSet
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
from service.framework.drf_class.custom_permission import CustomPermission
from service.request_service import RequestService
from ..helper.filter import NewsFilter
from ..models import News
from ..helper.sr import NewsSr, NewsDetailSr, NewsListSr
from module.article.category.helper.util import CategoryUtil
from module.article.news.consts import NEWS_TYPES, NEWS_STATUSS


class NewsViewSet(GenericViewSet):
    _name = "news"
    serializer_class = NewsSr
    filterset_class = NewsFilter
    _permission_alias = {
        "view": ["get_related"],
    }
    # permission_classes = (CustomPermission,)
    search_fields = ("title",)

    def get_extra(self):
        extra = {
            "options": {
                "categories": CategoryUtil.get_category_tree(),
                "types": NEWS_TYPES,
                "status": NEWS_STATUSS,
            }
        }
        return extra

    permission_classes=[AllowAny]
    def list(self, request):
        queryset = News.objects.all()
        queryset = self.filter_queryset(queryset)
        queryset = self.paginate_queryset(queryset)
        serializer = NewsListSr(queryset, many=True)

        result = {"items": serializer.data, "extra": self.get_extra()}
        return self.get_paginated_response(result)

    permission_classes=[AllowAny]
    def retrieve(self, request, pk=None):
        obj = get_object_or_404(News, pk=pk)
        serializer = NewsDetailSr(obj)
        return RequestService.res(serializer.data)

    @action(methods=["post"], detail=True)
    def add(self, request):
        staff = request.user.staff
        data = request.data
        data["created_by"] = staff.id
        data["updated_by"] = staff.id

        serializer = NewsSr(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return RequestService.res(serializer.data)

    @action(methods=["put"], detail=True)
    def change(self, request, pk=None):
        obj = get_object_or_404(News, pk=pk)

        staff = request.user.staff
        data = request.data
        data["updated_by"] = staff.id

        serializer = NewsSr(obj, data=data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return RequestService.res(serializer.data)

    @action(methods=["delete"], detail=True)
    def delete(self, request, pk=None):
        obj = get_object_or_404(News, pk=pk)
        obj.delete()
        return RequestService.res(status=status.HTTP_204_NO_CONTENT)

    @transaction.atomic
    @action(methods=["delete"], detail=False)
    def delete_list(self, request):
        pk = self.request.query_params.get("ids", "")
        pks = [int(pk)] if pk.isdigit() else [int(i) for i in pk.split(",")]
        for pk in pks:
            item = get_object_or_404(News, pk=pk)
            item.delete()
        return RequestService.res(status=status.HTTP_204_NO_CONTENT)

    @action(methods=["get"], detail=False)
    def get_related(self, request, pk=None):
        obj = get_object_or_404(News, pk=pk)
        related_news = (
            News.objects.filter(categories__in=obj.categories.all())
            .exclude(id=obj.id)
            .distinct()
        )
        related_news = self.filter_queryset(related_news)
        related_news = self.paginate_queryset(related_news)
        serializer = NewsDetailSr(related_news, many=True)

        result = {"items": serializer.data, "extra": self.get_extra()}
        return self.get_paginated_response(result)

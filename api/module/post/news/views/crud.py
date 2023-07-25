from django.db import transaction
from django.shortcuts import get_object_or_404
from module.dropdown.newsType.helper.util import NewsTypeUtil
from module.dropdown.newsCategory.helper.util import NewsCategoryUtil
from rest_framework.decorators import action
from rest_framework.viewsets import GenericViewSet
from rest_framework import status
from service.framework.drf_class.custom_permission import CustomPermission
from service.request_service import RequestService
from ..models import News
from ..helper.sr import NewsSr


class NewsViewSet(GenericViewSet):
    _name = "news"
    serializer_class = NewsSr
    permission_classes = (CustomPermission,)
    search_fields = ("title",)

    def list(self, request):
        queryset = News.objects.all()
        queryset = self.filter_queryset(queryset)
        queryset = self.paginate_queryset(queryset)
        serializer = NewsSr(queryset, many=True)
        
        news_categories = NewsCategoryUtil.get_news_category_tree()
        news_types = NewsTypeUtil.get_news_types()
        options = {}
        options["news_categories"] = news_categories
        options["news_types"] = news_types
        
        result = {
            "items": serializer.data, 
            "extra": {
                "options": options
            }
        }
        
        return self.get_paginated_response(result)

    def retrieve(self, request, pk=None):
        obj = get_object_or_404(News, pk=pk)   
        serializer = NewsSr(obj)
        return RequestService.res(serializer.data)

    @action(methods=["post"], detail=True)
    def add(self, request):
        serializer = NewsSr(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return RequestService.res(serializer.data)

    @action(methods=["put"], detail=True)
    def change(self, request, pk=None):
        obj = get_object_or_404(News, pk=pk)
        serializer = NewsSr(obj, data=request.data)
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
    
    @action(methods=["post"], detail=True)
    def inactivate(self, request, pk=None):
        News.objects.filter(pk=pk).update(status=0)
        obj = get_object_or_404(News, pk=pk)
        serializer = NewsSr(obj)

        return RequestService.res(serializer.data)
    
    @action(methods=["post"], detail=True)
    def activate(self, request, pk=None):
        News.objects.filter(pk=pk).update(status=1)
        obj = get_object_or_404(News, pk=pk)
        serializer = NewsSr(obj)

        return RequestService.res(serializer.data)

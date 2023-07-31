from rest_framework.serializers import ModelSerializer
from ..models import News
from module.article.news.consts import NEWS_TYPES

class NewsSr(ModelSerializer):
    class Meta:
        model = News
        exclude = ()
        read_only_fields = ("id",)


class NewsDetailSr(ModelSerializer):
    class Meta:
        model = News
        exclude = ()
        read_only_fields = ("id",)
    
    def to_representation(self, obj):
        rep = super().to_representation(obj)
        
        categories = obj.categories.all().order_by("-title")
        categories_obj = []
        for category in categories:
            categories_obj.append({
                "value": category.id,
                "label": category.title
            })

        rep["categories_obj"] = categories_obj
        
        rep["type_obj"] = next((x for x in NEWS_TYPES if x["value"] == obj.type), None)
        
        rep["created_by_obj"] = {
            "value": obj.created_by.id,
            "label": obj.created_by.full_name,
        }
        
        return rep
    
class NewsListSr(ModelSerializer):
    class Meta:
        model = News
        exclude = ()
        read_only_fields = ("id",)
    
    def to_representation(self, obj):
        rep = super().to_representation(obj)
        
        categories = obj.categories.all().order_by("-title")
        categories_obj = []
        for category in categories:
            categories_obj.append({
                "value": category.id,
                "label": category.title
            })

        rep["content"] = ""
        rep["categories_obj"] = categories_obj
        
        rep["type_obj"] = next((x for x in NEWS_TYPES if x["value"] == obj.type), None)
        
        rep["created_by_obj"] = {
            "value": obj.created_by.id,
            "label": obj.created_by.full_name,
        }
        
        return rep
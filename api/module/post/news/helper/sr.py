from rest_framework.serializers import ModelSerializer
from ..models import News


class NewsSr(ModelSerializer):
    class Meta:
        model = News
        exclude = ()
        read_only_fields = ("id",)
        
    def to_representation(self, obj):
        rep = super().to_representation(obj)
        rep["news_type_name"] = obj.news_type.name
        # user = obj.user

        return rep

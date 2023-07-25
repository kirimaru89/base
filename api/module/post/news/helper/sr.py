from module.dropdown.newsCategory.models import NewsCategory
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
        
        rep["news_categories"] = "; ".join(
                list(
                    NewsCategory.objects.filter(
                        pk__in= obj.news_category_ids
                    )
                    .order_by("name")
                    .values_list("name", flat=True),
                ),
            )
        # rep["news_category_name"] = obj.news_category.name
        rep["created_by_user"] = obj.created_by.user.full_name
        # user = obj.user

        return rep

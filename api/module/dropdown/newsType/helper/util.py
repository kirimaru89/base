from module.dropdown.newsType.helper.sr import NewsTypeSr
from module.dropdown.newsType.models import NewsType

class NewsTypeUtil:
    def get_news_types():
        news_types = NewsType.objects.order_by("id")
        serializer = NewsTypeSr(news_types, many=True)
        
        return serializer.data
    
    pass
       

from module.dropdown.newsCategory.models import NewsCategory


class NewsCategoryUtil:
    @staticmethod
    def get_news_category_tree():
        root_nodes = NewsCategory.objects.filter(parent_id__isnull=True).order_by('name')
        nodes = NewsCategoryUtil.get_news_type_with_child(root_nodes)
        
        return nodes
       
    @staticmethod
    def get_news_type_with_child(root_nodes):
        nodes = []
        for root_node in root_nodes:
            node = {
                "id": root_node.id,
                "name": root_node.name,
                "parentId": root_node.parent_id
            }
            
            children = NewsCategoryUtil.get_news_type_with_child(root_node.children.all().order_by('name'))
            node["is_leaf"] = len(children) == 0
            node["selectable"] = len(children) == 0
            node["children"] = children            
            
            nodes.append(node)
            
        return nodes

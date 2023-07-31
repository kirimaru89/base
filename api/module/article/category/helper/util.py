from module.article.category.models import Category

class CategoryUtil:
    @staticmethod
    def get_category_tree():
        root_nodes = Category.objects.filter(parent_id__isnull=True).order_by('title')
        nodes = CategoryUtil.get_categories_with_child(root_nodes)
        
        return nodes
    
    @staticmethod
    def get_categories_with_child(root_nodes):
        nodes = []
        for root_node in root_nodes:
            node = {
                "value": root_node.id,
                "label": root_node.title,
                "parentId": root_node.parent_id
            }
            
            children = CategoryUtil.get_categories_with_child(root_node.children.all().order_by('title'))
            node["is_leaf"] = len(children) == 0
            node["selectable"] = len(children) == 0
            node["children"] = children            
            
            nodes.append(node)
            
        return nodes
    
    pass

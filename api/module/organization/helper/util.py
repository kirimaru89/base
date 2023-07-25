from module.organization.models import Organization
from django.core.cache import cache

class OrganizationUtil:
    @staticmethod
    def get_organization_tree():
        cache_key = "Organization_treeview"
        nodes = cache.get(cache_key)
        
        if nodes is None:
            all_nodes = Organization.objects.all()
            root_nodes = all_nodes.filter(parent_id__isnull=True).order_by('name')
            nodes = OrganizationUtil.get_tree(root_nodes)
            cache.set(cache_key, nodes)
         
        return nodes
         
    @staticmethod
    def get_tree(root_nodes):
        nodes = []
        for root_node in root_nodes:
            node = {
                "id": root_node.id,
                "name": root_node.name,
                "parentId": root_node.parent_id
            }
            
            children = OrganizationUtil.get_tree(root_node.children.order_by('name'))
            node["is_leaf"] = len(children) == 0
            node["selectable"] = len(children) == 0
            node["children"] = children            
            
            nodes.append(node)
            
        return nodes
    pass
       

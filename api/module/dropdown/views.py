from rest_framework.views import APIView
from module.dropdown.helper.utils import DropdownUtils
from service.request_service import RequestService


class DropdownView(APIView):
    def get(self, request):
        result = DropdownUtils.get_options(user=request.user)
        return RequestService.res(result)

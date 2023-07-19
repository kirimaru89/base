from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from module.account.union_member.helper.sr import UnionMemberSr
from module.account.union_member.helper.util import UnionMemberUtil
from service.format_service import FormatService
from service.request_service import RequestService


class ProfileView(APIView):
    permission_classes = (IsAuthenticated,)

    def get_user(self):
        return self.request.user

    def get(self, request):
        union_member = self.get_user().union_member
        data = UnionMemberSr(union_member).data
        return RequestService.res(data)

    def put(self, request):
        user = self.get_user()
        union_member = user.union_member
        data = {}
        if phone_number := request.data.get("phone_number", None):
            data = dict(
                phone_number=FormatService.phone_to_canonical_format(phone_number)
            )
        union_member = UnionMemberUtil.update_union_member(union_member, data)
        sr = UnionMemberSr(union_member)
        return RequestService.res(sr.data)

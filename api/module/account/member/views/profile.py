from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from service.format_service import FormatService
from service.request_service import RequestService
from module.account.member.helper.sr import MemberProfileSr, MemberDetailSr
from module.account.member.helper.util import MemberUtil


class ProfileView(APIView):
    permission_classes = (IsAuthenticated,)

    def get_user(self):
        return self.request.user

    def get(self, request):
        member = self.get_user().member
        data = MemberProfileSr(member).data
        return RequestService.res(data)

    def put(self, request):
        user = self.get_user()
        member = user.member
        data = request.data
        if mobile := request.data.get("mobile", None):
            data["mobile"] = FormatService.phone_to_canonical_format(mobile)
        member = MemberUtil.update_member(member, data)
        sr = MemberProfileSr(member, context={"is_update": True})
        return RequestService.res(sr.data)

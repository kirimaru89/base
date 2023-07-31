from django.db import transaction
from django.utils.translation import gettext_lazy as _
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny

from module.account.member.helper.sr import RegistrationSr
from module.account.member.helper.util import MemberUtil
from module.account.user.helper.sr import UserDetailSr
from module.account.user.helper.util import UserUtil
from service.format_service import FormatService
from service.request_service import RequestService
from service.token_service import TokenService


class RegistrationView(APIView):
    permission_classes = (AllowAny,)

    @transaction.atomic
    def post(self, request, *args, **kwargs):
        data = request.data
        email = data.get("email", "").lower()
        mobile = data.get("mobile", "")

        mobile = FormatService.phone_to_canonical_format(mobile)
        if not FormatService.check_valid_phone_number(mobile):
            return RequestService.err({"detail": _("Invalid mobile format")})

        data["email"] = email
        data["mobile"] = mobile
        serializer = RegistrationSr(data=data)
        serializer.is_valid(raise_exception=True)
        if is_duplicate_username := UserUtil.is_duplicate_username(email):
            return RequestService.err(is_duplicate_username)

        member = MemberUtil.create_member(request.data)
        user = member.user
        refresh_token = TokenService.get_token_from_username(email)
        token = TokenService.refresh(refresh_token)
        response = RequestService.jwt_response_handler(token, refresh_token, user)
        response["user"] = UserDetailSr(user).data
        return RequestService.res(response)

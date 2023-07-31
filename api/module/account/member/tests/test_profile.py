import json
from rest_framework.test import APIClient
from django.test import TestCase
from service.format_service import FormatService
from module.account.member.helper.util import MemberUtil


class MemberProfileTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.anonClient = APIClient()
        self.base_url = "/api/v1/account/member/profile/"

    def test_view_profile(self):
        member_data = MemberUtil.seeding(1, True, False)
        member = MemberUtil.seeding(1, True)

        # Before authenticate
        resp = self.anonClient.get(self.base_url)
        self.assertEqual(resp.status_code, 401)

        # After authenticate
        self.client.force_authenticate(user=member.user)
        resp = self.client.get(self.base_url)

        status_code = resp.status_code
        self.assertEqual(status_code, 200)
        resp = resp.json()
        self.assertEqual(resp["email"], member_data["email"])

    def test_update_profile(self):
        member = MemberUtil.seeding(1, True)

        data = {"phone_number": "0906696555"}

        # Before authenticate
        resp = self.anonClient.put(
            self.base_url,
            json.dumps(data),
            content_type="application/json",
        )

        self.assertEqual(resp.status_code, 401)

        # After authenticate
        self.client.force_authenticate(user=member.user)
        resp = self.client.put(
            self.base_url,
            json.dumps(data),
            content_type="application/json",
        )

        status_code = resp.status_code
        resp = resp.json()
        self.assertEqual(status_code, 200)
        self.assertEqual(
            resp["phone_number"],
            FormatService.phone_to_canonical_format(data["phone_number"]),
        )

import json
from rest_framework.test import APIClient
from django.test import TestCase
from ..models import Member
from ..helper.util import MemberUtil

# Create your tests here.


class MemberTestCase(TestCase):
    def setUp(self):
        self.base_url = "/api/v1/account/member/"
        self.base_url_params = "/api/v1/account/member/{}"
        member = MemberUtil.seeding(1, True)
        member.user.is_member = True
        member.user.save()

        self.client = APIClient()
        self.client.force_authenticate(user=member.user)

        self.items = MemberUtil.seeding(3)

    def test_list(self):
        resp = self.client.get(self.base_url)
        self.assertEqual(resp.status_code, 200)
        resp = resp.json()
        self.assertEqual(resp["count"], 3)

    def test_detail(self):
        # Item not exist
        resp = self.client.get(self.base_url_params.format(0))
        self.assertEqual(resp.status_code, 404)

        # Item exist
        resp = self.client.get(self.base_url_params.format(self.items[0].pk))
        self.assertEqual(resp.status_code, 200)

    def test_create(self):
        item3 = MemberUtil.seeding(3, True, False)
        item4 = MemberUtil.seeding(4, True, False)

        # Add duplicate
        resp = self.client.post(
            self.base_url, json.dumps(item3), content_type="application/json"
        )
        self.assertEqual(resp.status_code, 400)

        # Add success
        resp = self.client.post(
            self.base_url, json.dumps(item4), content_type="application/json"
        )

        resp = resp.json()
        self.assertEqual(Member.objects.count(), 4)

    def test_edit(self):
        item2 = MemberUtil.seeding(2, True, False)

        # Update not exist
        resp = self.client.put(
            self.base_url_params.format(0),
            json.dumps(item2),
            content_type="application/json",
        )
        self.assertEqual(resp.status_code, 404)

        # Update duplicate
        resp = self.client.put(
            self.base_url_params.format(self.items[0].pk),
            json.dumps(item2),
            content_type="application/json",
        )
        self.assertEqual(resp.status_code, 400)

        # Update success
        resp = self.client.put(
            self.base_url_params.format(self.items[1].pk),
            json.dumps(item2),
            content_type="application/json",
        )
        self.assertEqual(resp.status_code, 200)

    def test_delete(self):
        # Remove not exist
        resp = self.client.delete(self.base_url_params.format(0))
        self.assertEqual(resp.status_code, 404)
        self.assertEqual(Member.objects.count(), 3)

        # Remove single success
        resp = self.client.delete(self.base_url_params.format(self.items[1].pk))
        self.assertEqual(resp.status_code, 204)
        self.assertEqual(Member.objects.count(), 2)

        # Remove list success
        resp = self.client.delete(
            (
                self.base_url
                + f'?ids={",".join([str(self.items[0].pk), str(self.items[2].pk)])}'
            )
        )

        self.assertEqual(resp.status_code, 204)
        self.assertEqual(Member.objects.count(), 0)

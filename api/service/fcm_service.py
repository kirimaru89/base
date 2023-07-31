from firebase_admin.exceptions import NotFoundError, InvalidArgumentError

from module.noti.device.models import DeviceToken
from module.noti.message.models import Message
from service.firebase_service import FirebaseService


class FcmService:
    @staticmethod
    def initialize_message(
        registration_token: str, device_type: str, data: dict, badge: int
    ):
        badge += 1
        messaging = FirebaseService().messaging
        data["badge"] = str(badge)
        notification = None
        apns = None
        if device_type == "ios":
            notification = messaging.Notification(data["title"], data["body"])
            apns = FcmService.get_apns(messaging, badge)
        return messaging.Message(
            data, notification, apns=apns, token=registration_token
        )

    @staticmethod
    def get_apns(messaging, badge):
        aps = messaging.Aps(badge=badge)
        apns_payload = messaging.APNSPayload(aps=aps)
        return messaging.APNSConfig(payload=apns_payload)

    @staticmethod
    def send_to_single_device(
        registration_token: str, device_type: str, data: dict, badge: int
    ):
        messaging = FirebaseService().messaging
        try:
            messaging.send(
                FcmService.initialize_message(
                    registration_token, device_type, data, badge
                )
            )
        except (NotFoundError, InvalidArgumentError):
            DeviceToken.objects.filter(registration_token=registration_token).delete()
        except Exception as e:
            print(repr(e))

    @staticmethod
    def send_multiple_and_write_messages(member, source_type, source_id):
        def inner(devices, data, badge):
            for device in devices:
                FcmService.send_to_single_device(
                    device.registration_token,
                    device.type,
                    data,
                    badge
                )
                Message.objects.create(
                    member=member,
                    title=data["title"],
                    content=data["content"],
                    source_type=source_type,
                    source_id=source_id,
                    data=data or {}
                )
        return inner

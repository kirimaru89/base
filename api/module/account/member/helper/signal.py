from custom_type import query_obj
from module.noti.verif.helper.util import VerifUtil


class MemberSignal:
    @staticmethod
    def pre_save(*args, **kwargs):
        pass

    @staticmethod
    def post_save(*args, **kwargs):
        if kwargs.get("created", False):
            member = kwargs.get("instance")
            MemberSignalutil.email_notification_after_creating(member)

    @staticmethod
    def pre_delete(*args, **kwargs):
        pass

    @staticmethod
    def post_delete(*args, **kwargs):
        pass


class MemberSignalutil:
    @staticmethod
    def email_notification_after_creating(member: query_obj):
        subject = "Tạo tài khoản thành công"
        to_email = member.user.email

        VerifUtil.send_noti_after_creating_email(subject, to_email)

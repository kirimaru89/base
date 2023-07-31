from django.apps import AppConfig
from django.db.models.signals import pre_save, post_save, pre_delete, post_delete


class MemberConfig(AppConfig):
    name = "module.account.member"

    def ready(self):
        from .helper.signal import MemberSignal

        sender = self.get_model("Member")

        pre_save.connect(MemberSignal.pre_save, sender=sender)
        post_save.connect(MemberSignal.post_save, sender=sender)
        pre_delete.connect(MemberSignal.pre_delete, sender=sender)
        post_delete.connect(MemberSignal.post_delete, sender=sender)

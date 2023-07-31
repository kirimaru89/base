from django.db.models import Q
from django.shortcuts import get_object_or_404
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import GenericViewSet

from service.date_service import DateService
from service.request_service import RequestService
from ..models import Message
from ..helper.sr import MessageSr


class MessageViewSet(GenericViewSet):
    _name = "message"
    serializer_class = MessageSr
    permission_classes = (AllowAny,)
    search_fields = ("title",)

    def list(self, request):
        user = request.user
        if user.is_anonymous:
            queryset = Message.objects.filter(member=None)
        else:
            queryset = Message.objects.filter(Q(member=user.member) | Q(member=None))
        queryset = self.filter_queryset(queryset)
        queryset = self.paginate_queryset(queryset)
        serializer = MessageSr(queryset, many=True)
        return self.get_paginated_response(serializer.data)

    def retrieve(self, request, pk=None):
        obj = get_object_or_404(Message, pk=pk)
        serializer = MessageSr(obj)
        return RequestService.res(serializer.data)

    @action(methods=["put"], detail=True)
    def mark_read(self, request):
        user = request.user
        pk = self.request.query_params.get("ids", "")
        pks = [int(pk)] if pk.isdigit() else [int(i) for i in pk.split(",")]
        query = Q(pk__in=pks, read_at=None)
        if user.is_anonymous:
            query &= Q(member=None)
        else:
            query &= (Q(member=user.member) | Q(member=None))
        Message.objects.filter(query).update(read_at=DateService.now())
        return RequestService.res({})

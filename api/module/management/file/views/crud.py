from django.db import transaction
from django.shortcuts import get_object_or_404
from django import forms
from rest_framework.decorators import action
from rest_framework.viewsets import GenericViewSet
from rest_framework import status

from service.aws_service import AwsService
from service.date_service import DateService
from rest_framework.permissions import AllowAny
from service.framework.drf_class.custom_permission import CustomPermission
from service.request_service import RequestService
from ..models import File
from ..helper.sr import FileSr
from django.http import HttpResponseRedirect
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
import uuid
import pathlib


class FileViewSet(APIView):
    # _name = "file"
    # serializer_class = FileSr
    permission_classes = (AllowAny,)
    # search_fields = ("title",)

    def post(self, request, *args, **kwargs):
        image_file = request.FILES.get("image")
        if image_file:
            file_extension = image_file.name.rsplit(".", 1)[1]
            epoch = str(DateService.epoch())
            file_name = f"file_{epoch}.{file_extension}"

            ok, url = AwsService.upload_file(key=file_name, body=image_file)
            if not ok:
                return Response({"message": "Something was wrong"}, status=400)

            return Response(
                {"message": "Image uploaded successfully", "image_path": url}
            )
        else:
            return Response({"message": "No image file provided"}, status=400)
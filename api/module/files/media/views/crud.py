from django.db import transaction
from django.shortcuts import get_object_or_404
from django import forms
from rest_framework.decorators import action
from rest_framework.viewsets import GenericViewSet
from rest_framework import status
from service.framework.drf_class.custom_permission import CustomPermission
from service.request_service import RequestService
from ..models import Media
from ..helper.sr import MediaSr
from django.http import HttpResponseRedirect
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
import uuid
import pathlib

class MediaViewSet(APIView):
    # _name = "media"
    # serializer_class = MediaSr
    # permission_classes = (CustomPermission,)
    # search_fields = ("title",)

    def post(self, request, *args, **kwargs):
        image_file = request.FILES.get('image')
        if image_file:
            current_domain = 'https://' + request.get_host()
            file_extension = pathlib.Path(image_file.name).suffix
            # Handle the file upload as needed
            # For example, save the file to disk or process it in some way
            file_path = f'media/{uuid.uuid4()}{file_extension}'
            with open(file_path, 'wb') as file:
                for chunk in image_file.chunks():
                    file.write(chunk)
            return Response({'message': 'Image uploaded successfully', 'image_path': f'{current_domain}/{file_path}'})
        else:
            return Response({'message': 'No image file provided'}, status=400)
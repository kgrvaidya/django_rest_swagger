from django.shortcuts import render
from .models import Floors, Projects, Blob
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .serializers import ProjectsSerializer, FloorSerializer, BlobSerializer
import coreapi
from rest_framework.schemas import AutoSchema
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser, FileUploadParser


class ProjectListSchema(AutoSchema):
    def get_manual_fields(self, path, method):
        extra_fields = []
        if method.lower() in ['post', 'put']:
            extra_fields = [coreapi.Field('name')]
        manual_fields = super().get_manual_fields(path, method)
        return manual_fields + extra_fields


class FloorsList(APIView):
    # parser_classes = (MultiPartParser, FormParser)

    def get(self, request):
        items = Floors.objects.all()
        serlaizer = FloorSerializer(items, many=True)
        return Response(serlaizer.data, status=200)
        
    # parser_classes = [JSONParser ]
    def post(self, request, format=None):
        data = request.data
        serializer = FloorSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
        # return Response(request.data)


class ProjectsList(APIView):
    schema = ProjectListSchema()

    def get(self, request):
        items = Projects.objects.all()
        serializer = ProjectsSerializer(items, many=True)
        return Response(serializer.data, status=200)

    def post(self, request):
        serializer = ProjectsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class ProjectDetail(APIView):
    def get(self, request, pk):
        item = Projects.objects.get(id=pk)
        serializer = ProjectsSerializer(item)
        return Response(serializer.data, status=200)

    def delete(self, request, pk):
        project = Projects.objects.get(id=pk)
        if project:
            project.delete()
            return Response(status=204)
        return Response(status=400)


class BlobDetail(APIView):
    def get(self, request):
        items = Blob.objects.all()
        serializer = BlobSerializer(items, many=True)
        return Response(serializer.data, status=200)

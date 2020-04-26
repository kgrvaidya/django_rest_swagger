from .models import Floors, Projects, Blob
from rest_framework import serializers


class ProjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = ['user_id', 'name', 'status']


class BlobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blob
        fields = ['floor_id', 'data']


class FloorSerializer(serializers.ModelSerializer):
    blobs = BlobSerializer(many=True, read_only=True)

    class Meta:
        model = Floors
        fields = ['house_id', 'type', 'name', 'blobs']

    def create(self, validated_data):
        if validated_data.get('blobs'):
            blob_data = validated_data.pop('blobs') | None
        floor = Floors.objects.create(**validated_data)
        if blob_data:
            for blobs in blob_data:
                Blob.objects.create(floor_id=floor, **blobs)
        return floor

from .models import Floors, Projects, Blob
from rest_framework import serializers


class ProjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = ['user_id', 'name', 'status']


class BlobSerializer(serializers.ModelSerializer):
    data = serializers.FileField()
    class Meta:
        model = Blob
        fields = ['floor_id', 'data']


class FloorSerializer(serializers.ModelSerializer):
    blobs = BlobSerializer(many=True, required=False)

    class Meta:
        model = Floors
        fields = ['id','house_id', 'type', 'name', 'blobs']

    def create(self, validated_data):
        blobs = validated_data.pop('blobs') if validated_data.get('blobs') else []
        floor = Floors.objects.create(**validated_data)
        for blob in blobs:
            Blob.objects.create(**blob, floor_id = floor)
        return floor

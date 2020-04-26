from .models import Floors, Projects, Blob
from rest_framework import serializers


class ProjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = ['user_id', 'name', 'status']

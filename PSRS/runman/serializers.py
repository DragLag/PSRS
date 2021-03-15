from rest_framework import serializers
from fileman.models import File
from background_task.models import Task


class ViewerFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ('file_name', 'version', 'file', 'pub_date')


class FileNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ['file_name']


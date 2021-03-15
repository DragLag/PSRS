from rest_framework.response import Response
from rest_framework import viewsets
from .serializers import ViewerFileSerializer, TasksSerializer
from background_task.models import Task
from fileman.models import File


class FileViewSet(viewsets.ViewSet):
    queryset = File.objects.all()
    serializer_class = ViewerFileSerializer()

    def list(self, request):
        """
        list all the uploaded eggs
        """
        queryset = File.objects.all()
        serializer = ViewerFileSerializer(queryset, many=True)
        return Response(serializer.data)


class TasksViewSet(viewsets.ViewSet):
    """
    retrieve:
    List all the uploaded eggs .
    """
    queryset = Task.objects.all()
    serializer_class = TasksSerializer()

    def list(self, request):
        """
        List all the executed jobs
        """
        queryset = Task.objects.all()
        serializer = TasksSerializer(queryset, many=True)
        return Response(serializer.data)

# Create your views here.

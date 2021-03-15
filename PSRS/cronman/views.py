from .serializers import CronSerializer
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from .models import Cron
from fileman.models import File



class CronEggViewSet(viewsets.ViewSet):
    """
    Example empty viewset demonstrating the standard
    actions that will be handled by a router class.

    If you're using format suffixes, make sure to also include
    the `format=None` keyword argument for each action.
    """
    serializer_class = CronSerializer
    queryset = Cron.objects.all()

    def list(self, request):
        """
        Return all the scheduled cron_jobs
        """
        queryset = Cron.objects.all()
        serializer = CronSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        """
        Create a new cron_job:
        """
        data = JSONParser().parse(request)
        serializer = CronSerializer(data=data)
        print(data)
        egg = File.objects.get(id=data['egg'])
        print(egg.file_name)
        if egg and serializer.is_valid():
            serializer.save()
            new_cron = Cron.objects.latest('id')
            response_text = {'cron_job_id': new_cron.id}
            return JsonResponse(response_text, status=201, safe=True)
        return JsonResponse(serializer.errors, status=400)

    def retrieve(self, request, pk=None):
        """
        retrieve a cron_job given an cron_job id
        """
        queryset = Cron.objects.all()
        egg = get_object_or_404(queryset, pk=pk)
        serializer = CronSerializer(egg)
        return Response(serializer.data)

    def update(self, request, pk=None):
        """
        update a cron_job given a cron_job id
        """
        data = JSONParser().parse(request)
        egg = Cron.objects.get(pk=pk)
        if egg:
            egg.cron_string = data['cron_string']
            egg.save()
            response_text = {'cron_job_id': egg.id}
            return JsonResponse(response_text, status=201, safe=True)
        response_text = {'message': 'trigger was not updated'}
        return JsonResponse(response_text, status=400, safe = True)


    def destroy(self, request, pk=None):
        """
        delete a cron_job given a cron_job id
        """
        egg = Cron.objects.get(pk=pk)
        if egg:
            egg.delete()
            response_text = {'message': 'trigger deleted correctly'}
            return JsonResponse(response_text, status=201, safe=True)
        response_text = {'message': 'trigger does not exists'}
        return JsonResponse(response_text, status=400, safe=True)

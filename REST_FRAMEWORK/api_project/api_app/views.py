from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api_app.models import *
from api_app.serializers import *
# Create your views here.

@api_view(['GET'])
def task_list(request):
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks,many=True)
    return Response(serializer.data)


@api_view(['GET'])
def task_details(request,task_id):
    task_details = Task.objects.get(id=task_id)
    serializer = TaskSerializer(task_details,many=False)
    return Response(serializer.data)


@api_view(['POST'])
def task_create(request):
    serializer = TaskSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)



@api_view(['POST'])
def task_update(request,update_id):
    update = Task.objects.get(id= update_id)
    serializer = TaskSerializer(instance=update,data = request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def task_delete(request,delete_id):
    update = Task.objects.get(id= delete_id)
    update.delete()
    return Response('Item successfully Deleted..')
from rest_framework import viewsets
from .models import Task
from .serializers import TaskSerializer
from django.shortcuts import render, get_object_or_404


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all().order_by('title')
    serializer_class = TaskSerializer


def login(request):
    return render(request, "faketrello/login.html")


def tasks(request):
    return render(request, "faketrello/createTasks.html")

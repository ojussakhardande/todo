from django.shortcuts import render,redirect
from django.http import HttpResponse
from . import models

# Create your views here.
def add_todo(request):
    task=request.POST['tasK']
    models.task.objects.create(task=task)
    return redirect('home')

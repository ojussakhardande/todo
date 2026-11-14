from django.shortcuts import render
from todoapp import models


def home(request):
    task=models.task.objects.filter(is_completed=False).order_by('-updated_at')
    context={
        'tasks':task
    }
    return render(request, 'home.html',context)
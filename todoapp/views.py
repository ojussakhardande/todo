from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from . import models

# Create your views here.
def add_todo(request):
    task=request.POST['tasK']
    models.task.objects.create(task=task)
    return redirect('home')

def update_todo(request,id):
    models.task.objects.filter(id=id).update(is_completed=True)
    return redirect('home')

def delete(request,id):
    models.task.objects.filter(id=id).delete()
    return redirect('home')

def incomplete(request,id):
    task= get_object_or_404(models.task,id=id)
    task.is_completed = False
    task.save()
    return redirect('home')

def edit(request,id):
    tasks= get_object_or_404(models.task,id=id)
    context={
        'edit':tasks
    }
    if request.method == 'POST':
        tasks.task=request.POST['task']
        tasks.save()
        return redirect('home')
    elif request.method=='GET':
        pass
    return render(request,'edit.html',context)


    
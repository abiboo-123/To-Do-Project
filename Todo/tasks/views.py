from django.shortcuts import render, redirect
from . import models
from .forms import taskForm
# Create your views here.

def index(request):
    tasks = models.task.objects.all()
    form = taskForm()
    
    if request.method == 'POST':
        form = taskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    
    context = {'tasks': tasks, 'form': form}
    return render(request, 'index.html', context)

def ubdateTask(request, pk):
    task = models.task.objects.get(id=pk)
    form = taskForm(instance=task)
    
    if request.method == "POST":
        form = taskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('/')
    
    context = {'form': form}
    return render(request, 'update_task.html', context)
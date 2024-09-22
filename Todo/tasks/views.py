from django.shortcuts import render, redirect
from .models import task
from .forms import taskForm
# Create your views here.

def main(request):
    tasks = task.objects.all()
    form = taskForm()
    
    if request.method == 'POST':
        form = taskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    
    context = {'tasks': tasks, 'form': form}
    return render(request, 'index.html', context)
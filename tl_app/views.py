from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Task
from .forms import TaskForm



# Create your views here.

def task_list(request):
    tasks = Task.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
    return render(request, 'task_list.html', {'tasks': tasks})

def task_detail(request, pk):
    task = get_object_or_404(Task, pk=pk)
    return render(request, 'task_detail.html', {'task': task})

def task_new(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'task_new.html', {'form':form})

def task_edit(request,pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == "POST":
        form = TaskForm(request.POST, instance = task)
        if form.is_valid():
            form.save()
            return redirect('task_detail', pk=task.pk)
    else:
        form = TaskForm(instance = task)
    return render(request, 'task_edit.html', {'form': form})
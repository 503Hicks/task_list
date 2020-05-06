from django.shortcuts import render
from django.utils import timezone
from .models import Task

# Create your views here.

def task_list(request):
    tasks = Task.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
    return render(request, 'task_list.html', {'tasks':tasks})


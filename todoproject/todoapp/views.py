from django.shortcuts import render, redirect
from .forms import Todoform
from .models import Task

# -----------------------------------------------------------
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView


# -----------------------------------------------------------

# Create your views here.
def add(request):
    if request.method == 'POST':
        name = request.POST.get('task', '')
        priority = request.POST.get('priority', '')
        date = request.POST.get('date', '')
        task = Task(name=name, priority=priority, date=date)
        task.save()
        return redirect('/')
    task = Task.objects.all()
    return render(request, 'home.html', {'task': task})


def delete(request, taskid):
    task = Task.objects.get(id=taskid)
    if request.method == 'POST':
        task.delete()
        return redirect('/')
    return render(request, "delete.html")


def update(request, taskid):
    task = Task.objects.get(id=taskid)
    form = Todoform(request.POST or None, request.FILES, instance=task)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'update.html', {'form': form, 'task': task})


# -------------------------------------------------------------------------------------------------

class Tasklistview(ListView):
    model = Task
    template_name = 'home.html'
    context_object_name = 'task'


class TaskDetailview(DetailView):
    model = Task
    template_name = 'detail.html'
    context_object_name = 'task'


class TaskUpdateview(UpdateView):
    model = Task
    template_name = 'update.html'
    context_object_name = 'task'
    fields = ('name','priority','date')

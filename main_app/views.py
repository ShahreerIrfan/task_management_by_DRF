from django.shortcuts import render
def home(request):
    return render(request,'main_app/index.html')

from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView
from .models import Task
from django.urls import reverse_lazy
from .forms import TaskUpdateForm
class TaskCreateView(CreateView):
    model = Task
    fields = ['title', 'description', 'due_date', 'priority', 'photos']

class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskUpdateForm
    template_name = 'main_app/task_update.html'
    success_url = reverse_lazy('task-list')


class TaskDeleteView(DeleteView):
    model = Task
    success_url = reverse_lazy('task-list')

class TaskListView(ListView):
    model = Task
    template_name = 'main_app/task_list.html'

class TaskDetailView(DetailView):
    model = Task
    template_name = 'main_app/task_detail.html'



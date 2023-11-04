from django.shortcuts import render
from .forms import TaskCreateForm,TaskUpdateForm,CustomPasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request,'main_app/index.html')

from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView
from .models import Task
from django.urls import reverse_lazy
from .forms import TaskUpdateForm
class TaskCreateView(CreateView):
    model = Task
    form_class = TaskCreateForm
    template_name = 'main_app/task_create.html'  # Create this template
    success_url = reverse_lazy('task-list')
    def form_valid(self, form):
        # Set the owner to the currently logged-in user
        form.instance.owner = self.request.user
        return super().form_valid(form)


def home(request):
    return render(request,'main_app/index.html')

class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskUpdateForm
    template_name = 'main_app/task_update.html'
    success_url = reverse_lazy('task-list')


class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'main_app/task_detail.html'  # Template to render after deletion
    success_url = reverse_lazy('task-list')

class TaskListView(ListView):
    model = Task
    template_name = 'main_app/task_list.html'

class TaskDetailView(DetailView):
    model = Task
    template_name = 'main_app/task_detail.html'

from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from .forms import RegistrationForm, LoginForm

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # Replace 'home' with your actual homepage URL
    else:
        form = RegistrationForm()
    return render(request, 'main_app/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')  # Replace 'home' with your actual homepage URL
    else:
        form = LoginForm()
    return render(request, 'main_app/login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('login')

class CustomPasswordChangeView(PasswordChangeView):
    form_class = CustomPasswordChangeForm
    template_name = 'main_app/password_change.html'



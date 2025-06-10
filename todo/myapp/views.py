from django.shortcuts import render, get_object_or_404, redirect
from .models import Tasks
from .forms import TaskForm , UserRegisterForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login

def index(request):
    return render(request, 'management.html')

def task_list(request):
    tasks = Tasks.objects.all()
    return render(request, 'task_list.html', {'tasks': tasks})

@login_required
def create_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST, request.FILES)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'task_form.html', {'form': form})

@login_required
def edit_task(request, task_id):  # changed user_id -> task_id
    task = get_object_or_404(Tasks, pk=task_id, user=request.user)
    if request.method == "POST":
        form = TaskForm(request.POST, request.FILES, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'task_form.html', {'form': form})

@login_required
def delete_task(request, task_id):  # changed user_id -> task_id
    task = get_object_or_404(Tasks, pk=task_id, user=request.user)
    if request.method == "POST":
        task.delete()
        return redirect('task_list')
    return render(request, 'delete_task.html', {'task': task})

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            login(request , user)
            return redirect('task_list')
    else:
        form = UserRegisterForm()
    return render(request, 'registration/register.html' , {'form' : form})

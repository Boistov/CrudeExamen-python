from django.shortcuts import render, get_object_or_404, redirect
from .models import User, Task

def user_list(request):
    users = User.objects.all()
    return render(request, 'user_list.html', {'users': users})

def user_create(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        User.objects.create(username=username, email=email, password=password)
        return redirect('user_list')
    return render(request, 'user_create.html')

def user_update(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        user.username = request.POST['username']
        user.email = request.POST['email']
        user.password = request.POST['password']
        user.save()
        return redirect('user_list')
    return render(request, 'user_update.html', {'user': user})

def user_delete(request, pk):
    user = get_object_or_404(User, pk=pk)
    user.delete()
    return redirect('user_list')

def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'task_list.html', {'tasks': tasks})

def task_create(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        user_id = request.POST['user']
        user = get_object_or_404(User, pk=user_id)
        Task.objects.create(title=title, description=description, user=user)
        return redirect('task_list')
    users = User.objects.all()
    return render(request, 'task_create.html', {'users': users})

def task_update(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task.title = request.POST['title']
        task.description = request.POST['description']
        task.completed = 'completed' in request.POST
        user_id = request.POST['user']
        task.user = get_object_or_404(User, pk=user_id)
        task.save()
        return redirect('task_list')
    users = User.objects.all()
    return render(request, 'task_update.html', {'task': task, 'users': users})

def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect('task_list')

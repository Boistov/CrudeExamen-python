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
    return render(request, 'user.html')

def user_update(request):
    if request.method == 'POST':
        user_id = request.POST['user_id']
        user = get_object_or_404(User, id=user_id)
        user.username = request.POST['username']
        user.email = request.POST['email']
        user.password = request.POST['password']
        user.save()
        return redirect('user_list')
    users = User.objects.all()
    return render(request, 'user_update.html', {'users': users})

def user_delete(request):
    if request.method == 'POST':
        user_id = request.POST['user_id']
        user = get_object_or_404(User, id=user_id)
        user.delete()
        return redirect('user_list')
    users = User.objects.all()
    return render(request, 'user_delete.html', {'users': users})

def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'task_list.html', {'tasks': tasks})

def task_create(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        user_id = request.POST['user']
        user = get_object_or_404(User, id=user_id)
        Task.objects.create(title=title, description=description, user=user)
        return redirect('task_list')
    users = User.objects.all()
    return render(request, 'task.html', {'users': users})

def task_update(request):
    if request.method == 'POST':
        task_id = request.POST['task_id']
        task = get_object_or_404(Task, id=task_id)
        task.title = request.POST['title']
        task.description = request.POST['description']
        task.completed = 'completed' in request.POST
        user_id = request.POST['user']
        task.user = get_object_or_404(User, id=user_id)
        task.save()
        return redirect('task_list')
    tasks = Task.objects.all()
    users = User.objects.all()
    return render(request, 'task_update.html', {'tasks': tasks, 'users': users})

def task_delete(request):
    if request.method == 'POST':
        task_id = request.POST['task_id']
        task = get_object_or_404(Task, id=task_id)
        task.delete()
        return redirect('task_list')
    tasks = Task.objects.all()
    return render(request, 'task_delete.html', {'tasks': tasks})

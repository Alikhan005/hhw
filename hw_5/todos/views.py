from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Todo
from .forms import TodoForm
from django.shortcuts import render

def home_view(request):
    return render(request, 'home.html')


def login_page(request):
    return render(request, 'todos/login.html')

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('todos_list')
    return redirect('login')

def logout_user(request):
    logout(request)
    return redirect('login')

@login_required
def todos_list(request):
    todos = Todo.objects.filter(user=request.user)
    return render(request, 'todos.html', {'todos': todos})

@login_required
def todo_detail(request, todo_id):
    todo = get_object_or_404(Todo, id=todo_id, user=request.user)
    return render(request, 'todo_detail.html', {'todo': todo})

@login_required
def add_todo(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.user = request.user
            todo.save()
            return redirect('todos_list')
    else:
        form = TodoForm()
    return render(request, 'add_todo.html', {'form': form})

@login_required
def delete_todo(request, todo_id):
    todo = get_object_or_404(Todo, id=todo_id, user=request.user)
    todo.delete()
    return redirect('todos_list')

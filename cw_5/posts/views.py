from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.http import HttpResponseForbidden
from .models import Post
from .forms import PostForm
from django.shortcuts import render, redirect 

def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully! You can now log in.')
            return redirect('login')  # Перенаправление на страницу входа
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def login_page(request):
    return render(request, 'login.html')

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('posts')  # Перенаправление на страницу постов
        else:
            messages.error(request, 'Invalid credentials')
    return render(request, 'login.html')

def logout_user(request):
    logout(request)
    return redirect('login')

@login_required
def posts_list(request):
    posts = Post.objects.all()
    return render(request, 'posts/list.html', {'posts': posts})

@login_required
def my_posts(request):
    posts = Post.objects.filter(author=request.user)
    return render(request, 'posts/my_posts.html', {'posts': posts})

@login_required
def post_detail(request, id):
    post = get_object_or_404(Post, id=id)
    is_author = post.author == request.user
    is_admin = request.user.is_superuser
    return render(request, 'posts/detail.html', {'post': post, 'is_author': is_author, 'is_admin': is_admin})

@login_required
def create_post(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            messages.success(request, 'Post created successfully!')
            return redirect('posts')
    else:
        form = PostForm()
    return render(request, 'posts/create.html', {'form': form})

@login_required
def delete_post(request, id):
    post = get_object_or_404(Post, id=id)
    if post.author == request.user or request.user.is_superuser:
        post.delete()
        messages.success(request, 'Post deleted successfully!')
        return redirect('posts')
    return HttpResponseForbidden()
def home(request):
    return redirect('posts')  # Перенаправляем на страницу с постами
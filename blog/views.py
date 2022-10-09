from django.shortcuts import render, redirect
from .forms import SignupForm, LoginForm, PostForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import Post
from datetime import datetime

# Home View
def home(request):
    data = Post.objects.all()
    return render(request, 'blog/home.html', {'data': data})

# About View
def about(request):
    return render(request, 'blog/about.html')

# Signup View
def signup(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            fm = SignupForm(request.POST)
            if fm.is_valid():
                fm.save()
                return redirect('login')
        else:
            fm = SignupForm()
        return render(request, 'blog/signup.html', {'form':fm})

# Login View
def user_login(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            fm = LoginForm(request=request, data=request.POST)
            if fm.is_valid():
                username = fm.cleaned_data.get('username')
                password = fm.cleaned_data.get('password')
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    messages.success(request, f'Welcome {username}. You are logged in.')
                    return redirect('home')
        else:
            fm = LoginForm()
        return render(request, 'blog/login.html', {'form': fm})

# Logout View
def user_logout(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request, 'Your are logged out.')
        return redirect('login')
    else:
        return redirect('login')

# Add Post View
def add_post(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            fm = PostForm(data=request.POST)
            if fm.is_valid():
                username = request.user.username
                tittle = fm.cleaned_data.get('tittle')
                desc = fm.cleaned_data.get('description')
                dt = datetime.now()
                date = dt.date()
                reg = Post(user_name=username, tittle=tittle, description=desc, date=date)
                reg.save()
                messages.success(request, 'Your post has been uploaded.')
                return redirect('home')
        else:
            fm = PostForm()
        return render(request, 'blog/add_post.html', {'form': fm})
    else:
        return redirect('login')

# Update View
def update_post(request, id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            fm = PostForm(data=request.POST)
            if fm.is_valid():
                username = request.user.username
                tittle = fm.cleaned_data.get('tittle')
                desc = fm.cleaned_data.get('description')
                dt = datetime.now()
                date = dt.date()
                reg = Post(id=id, user_name=username, tittle=tittle, description=desc, date=date)
                reg.save()
                messages.success(request, 'Your post has been updated.')
                return redirect('home')
        else:
            post = Post.objects.get(pk=id)
            if post.user_name != request.user.username:
                messages.error(request, 'You are not the author of this post.')
                return redirect('home')
            else:
                fm = PostForm(instance=post)
        return render(request, 'blog/update_post.html', {'form': fm})
    else:
        return redirect('login')

# Delete View
def delete_post(request, id):
    if request.user.is_authenticated:
        post = Post.objects.get(pk=id)
        if post.user_name != request.user.username:
            messages.error(request, 'You are not the author of this post.')
            return redirect('home')
        else:
            if request.method == 'POST':
                post = Post(id=id)
                post.delete()
            messages.success(request, 'Your post has been deleted.')
            return redirect('home')
    else:
        return redirect('login')
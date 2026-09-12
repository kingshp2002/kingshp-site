from django.db.models import F
from django.shortcuts import get_object_or_404, render, redirect
from .models import Post
from .forms import *
from django.contrib.auth.models import Group
from django.contrib.auth import authenticate, login, logout
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import login_required





@login_required
def post_edit(request, slug):

    post = get_object_or_404(
        Post,
        slug=slug
    )

    if not is_author(request.user):
        raise PermissionDenied

    if post.author != request.user:
        raise PermissionDenied

    if request.method == 'POST':
        form = PostForm(
            request.POST,
            instance=post
        )

        if form.is_valid():
            form.save()

            return redirect(
                'post_detail',
                slug=post.slug
            )

    else:
        form = PostForm(instance=post)

    return render(
        request,
        'blog/post_edit.html',
        {'form': form}
    )


@login_required
def post_delete(request, slug):

    post = get_object_or_404(
        Post,
        slug=slug
    )

    if not is_author(request.user):
        raise PermissionDenied

    if post.author != request.user:
        raise PermissionDenied

    if request.method == 'POST':
        post.delete()

        return redirect('/admin/')

    return render(
        request,
        'blog/post_delete.html',
        {'post': post}
    )





@login_required
def post_create(request):

    if not is_author(request.user):
        raise PermissionDenied
    if request.method == 'POST':
        form = PostForm(request.POST)

        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()

            return redirect(
                'post_detail',
                slug=post.slug
            )

    else:
        form = PostForm()

    return render(
        request,
        'blog/post_create.html',
        {'form': form}
    )

def post_detail(request, slug):
    post = get_object_or_404(
        Post,
        slug=slug,
        published=True
    )

    Post.objects.filter(pk=post.pk).update(
        views=F('views') + 1
    )

    post.refresh_from_db()

    return render(
        request,
        'blog/post_detail.html',
        {'post': post}
    )

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            user = form.save()
            readers_group = Group.objects.get(name='Readers')
            user.groups.add(readers_group)
            login(request, user)

            return redirect('home:index')

    else:
        form = RegisterForm()

    return render(
        request,
        'blog/register.html',
        {'form': form}
    )
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)
            return redirect('/blog/')

    return render(request, 'blog/login.html')
def blog(request):
    posts = Post.objects.filter(published=True).order_by('-created_at')
    return render(request, 'blog/blog.html', {'posts': posts})
def logout_view(request):
    logout(request)
    return redirect('/blog/login/')
def is_author(user):
    return user.groups.filter(name='Authors').exists()
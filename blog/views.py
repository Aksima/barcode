from django.contrib.auth.models import User, AnonymousUser
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseForbidden
from django.utils import timezone
from .forms import PostForm
from .models import Post


def post_list(request):
    if isinstance(request.user, AnonymousUser):
        request_user = User.objects.get(username='guest')
    else:
        request_user = request.user
    posts = (
        getattr(Post, 'objects').filter(
            published_date__lte=timezone.now()
        ).order_by('-published_date')
    )
    return render(
        request, 'blog/posts.html',
        {
            'posts': posts,
            'request_user': request_user
        }
    )


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})


def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            if isinstance(request.user, AnonymousUser):
                post.author = User.objects.get(username='guest')
            else:
                post.author = request.user
            post.publish()
            return redirect('blog:post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_new.html', {'form': form})


def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if isinstance(request.user, AnonymousUser):
        request_user = User.objects.get(username='guest')
    else:
        request_user = request.user
    if request_user != post.author:
        raise HttpResponseForbidden
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request_user
            post.publish()
            return redirect('blog:post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

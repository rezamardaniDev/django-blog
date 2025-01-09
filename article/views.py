from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Post

# Create your views here.

def home_view(request):
    posts = Post.objects.filter(status='published').order_by('post_view')
    return render(request, 'article/posts_list.html', context={'posts': posts})


def post_view(request, post_id):
    try:
        post = Post.objects.get(id=post_id)
    except Post.DoesNotExist:
        return render(request, 'article/404.html', status=404)
    
    post.post_view += 1
    post.save()
    return render(request, 'article/post_detail.html', context={'post': post})


def add_post(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        post = Post.objects.create(title=title, description=description)
        return redirect('/articles/') 
    return render(request, 'article/add_post.html')
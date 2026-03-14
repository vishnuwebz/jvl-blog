from django.shortcuts import render, get_object_or_404
from .models import Post


def index(request):
    posts = Post.objects.all()
    context = {
        "blog_title": "Latest Posts",
        "posts": posts,
    }
    return render(request, "blog/index.html", context)


def detail(request, slug: str):
    post = get_object_or_404(Post, slug=slug)
    context = {
        "post": post,
        "blog_title": post.title,
    }
    return render(request, "blog/detail.html", context)

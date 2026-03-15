from django.shortcuts import render, get_object_or_404
from .models import Post
from django.core.paginator import Paginator

def index(request):
    post_list = Post.objects.all()

    paginator = Paginator(post_list, 3)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        "blog_title" : "Latest Posts",
        "page_obj" : page_obj,
    }

    return render(request, "blog/index.html", context)

def detail(request, slug: str):
    post = get_object_or_404(Post, slug=slug)
    context = {
        "post": post,
        "blog_title": post.title,
    }
    return render(request, "blog/detail.html", context)

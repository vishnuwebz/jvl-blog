from django.shortcuts import render, get_object_or_404
from .models import Post, Category, Tag
from django.core.paginator import Paginator

def posts_by_category(request, category_slug: str):
    category = get_object_or_404(Category, slug=category_slug)
    posts = Post.objects.filter(categories__slug=category_slug).distinct()

    context = {
        "blog_title": f"Posts in {category.name}",
        "category": category,
        "posts": posts,
    }
    return render(request, "blog/posts_by_category.html", context)

def posts_by_tag(request, tag_slug: str):
    tag = get_object_or_404(Tag, slug=tag_slug)
    posts = Post.objects.filter(tags__slug=tag_slug).distinct()

    context = {
        "blog_title": f"Posts tagged #{tag.name}",
        "tag": tag,
        "posts": posts,
    }
    return render(request, "blog/posts_by_tag.html", context)

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

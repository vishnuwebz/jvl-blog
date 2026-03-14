from django.shortcuts import render, get_object_or_404
from django.http import Http404


POSTS = [
    {
        "id": 1,
        "title": "Getting started with Django",
        "excerpt": "Learn how to set up your first Django project and understand the basic structure.",
    },
    {
        "id": 2,
        "title": "Understanding Django templates",
        "excerpt": "A practical guide to Django’s template language, blocks, and inheritance.",
    },
    {
        "id": 3,
        "title": "Working with URL patterns",
        "excerpt": "Map clean URLs to Python views using path, converters, and named routes.",
    },
    {
        "id": 4,
        "title": "Styling your Django app",
        "excerpt": "Serve static files correctly and apply a consistent layout across pages.",
    },
]


def index(request):
    context = {
        "blog_title" : "Latest Posts",
        "posts": POSTS,
    }
    return render(request, "blog/index.html", context)


def detail(request, post_id: int):
    post = get_post_or_404(post_id)

    context = {
        "post":post,
        "blog_title": post["title"],
    }
    return render(request, "blog/detail.html", context)

def get_post_or_404(post_id: int):
    """ Simple helper until we switch to models."""
    for post in POSTS:
        if post["id"] == post_id:
            return post
    raise Http404("Post not found")
from django.urls import path
from . import views

app_name = "blog" # allows namespacing in templates (blog:index, blog:detail).

urlpatterns = [
    path("", views.index, name="index"),
    path("post/<slug:slug>/", views.detail, name="detail"),
]
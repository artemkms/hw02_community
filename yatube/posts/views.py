from django.shortcuts import render, get_object_or_404

from .models import Post, Group


def index(request):
    posts = Post.objects.all()[:10]
    return render(request, "index.html", {"posts": posts})


def group_posts(request, group_slug):
    group = get_object_or_404(Group, slug=group_slug)
    posts = group.posts.all()[:12]
    context = {"group": group, "posts": posts}
    return render(request, "group.html", context)

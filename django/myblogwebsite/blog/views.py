from .models import Post
from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .forms import ContactForm, PostForm


def post_list(request):
    posts = Post.objects.all()
    return render(request, "blog/posts_list.html", {"posts": posts})


def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, "blog/post_detail.html", {"post": post})


def post_search(request):
    query = request.GET.get("q", "")
    if query:
        posts = Post.objects.filter(
            Q(title__icontains=query) | Q(text__icontains=query)
        )
    else:
        posts = Post.objects.none()
    return render(request, "blog/posts_list.html", {"posts": posts})


def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
    else:
        form = ContactForm()
    return render(request, "blog/contact.html", {"form": form})


def post_create(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
    else:
        form = PostForm()
    return render(request, "blog/post_form.html", {"form": form})

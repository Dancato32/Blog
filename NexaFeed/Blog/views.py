from django.shortcuts import render
from .models import Post,Category,Comment



def index(request):
    posts=Post.objects.all().order_by("-created_at")
    context={
        'posts': posts,   
        }
    
    return render(request, 'Blog/index.html')
# Create your views here.



def blog_category(request, category):
    posts = Post.objects.filter(
        categories__name__contains=category
    ).order_by("-created_at")
    context = {
        "category": category,
        "posts": posts,
    }
    return render(request, "category.html", context)






def blog_detail(request, pk):
    post = Post.objects.get(pk=pk)
    comments = Comment.objects.filter(post=post)
    context = {
        "post": post,
        "comments": comments,
    }

    return render(request, "blog/detail.html", context)
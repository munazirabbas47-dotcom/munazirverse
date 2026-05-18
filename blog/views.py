from django.shortcuts import render
from django.http import HttpResponse
from .admin import BlogPost



# Create your views here.

def blogHome(request):
    allblog = BlogPost.objects.all()
    return render(request, "blog/index.html",{"allblog":allblog})

def blogPost(request,slug):
    post = BlogPost.objects.filter(slug=slug).first()
    
    return render(request, "blog/blogpost.html",{"post":post})
    

# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from article.models import Article
from datetime import datetime
from django.http import Http404

# Create your views here.
def home(request):
    post_list = Article.objects.all()
    return render(request, 'home.html', {'post_list': post_list})

def detail(request, my_args):
    print (my_args)
    post = Article.objects.get(id=int(my_args))
    return render(request, 'post.html', {'post': post})

def aboutMe(request):
    return render(request, 'aboutme.html')

def search_tag(request, tag) :
    post_list = Article.objects.filter(category = tag) #contains
    return render(request, 'tag.html', {'post_list' : post_list})

    

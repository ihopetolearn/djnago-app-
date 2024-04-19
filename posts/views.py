from django.shortcuts import render
from django.http import HttpResponse
from .models import post

def index(request):
    return HttpResponse('<h1> this is the index wab page and can be good </h1>')

def home(request):
    return HttpResponse('<h3> this is the home page </h3>')

def post_list(request):
    return render(request, 'posts/post_list.html', context={'key': (post.objects.all())})

def post_datail(request,pk):
    return render(request,'posts/post_detail.html',context={'key2':post.objects.get(pk=pk)})
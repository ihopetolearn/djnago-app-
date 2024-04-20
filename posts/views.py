from django.shortcuts import render, HttpResponseRedirect
from django.http import HttpResponse
from .models import post
from .forms import PostForms, Test

def index(request):
    return HttpResponse('<h1> This is the index web page and can be good </h1>')

def home(request):
    return HttpResponse('<h3> This is the home page </h3>')

def post_list(request):
    return render(request, 'posts/post_list.html', context={'key': post.objects.all()})

def post_detail(request, pk):
    return render(request, 'posts/post_detail.html', context={'key2': post.objects.get(pk=pk)})

def post_create(request):
    if request.method == 'POST':
        form = PostForms(request.POST)  # Corrected 'request.POST' here
        if form.is_valid():
            post.objects.create(**form.cleaned_data)
            return HttpResponseRedirect('/posts/')
    else:
        form = PostForms()
    return render(request, 'posts/post_creat.html', {'form': form})  # Corrected 'post_create.html' here

def test_create(request):
    if request.method == 'POST':
        form = Test(request.POST)
        if form.is_valid():
            post.objects.create(**form.cleaned_data)
        return HttpResponseRedirect('/posts/')
    else:
        form = Test()
        return render(request,'posts/post_test.html',{'context':form})

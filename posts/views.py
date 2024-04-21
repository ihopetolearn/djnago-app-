from django.shortcuts import render, HttpResponseRedirect
from django.http import HttpResponse
from .models import Post
from .forms import PostForms, Test
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import PostSerializer1,PostSerializer2


@api_view(['GET'])
def index(request):
    try:
        p = Post.objects.all()
        # return Response({'post_id': p.id, 'title': p.title}, status=status.HTTP_202_ACCEPTED)
        serializer = PostSerializer1(p,many=True)
        return Response(serializer.data)
    except Post.DoesNotExist:
        return Response({'error': 'post_not_found'}, status=status.HTTP_400_BAD_REQUEST)

def home(request):
    return HttpResponse('<h3> This is the home page </h3>')

def post_list(request):
    return render(request, 'posts/post_list.html', context={'key': Post.objects.all()})

def post_detail(request, pk):
    return render(request, 'posts/post_detail.html', context={'key2': Post.objects.get(pk=pk)})

def post_create(request):
    if request.method == 'POST':
        form = PostForms(request.POST)  # Corrected 'request.POST' here
        if form.is_valid():
            Post.objects.create(**form.cleaned_data)
            return HttpResponseRedirect('/posts/')
    else:
        form = PostForms()
    return render(request, 'posts/post_creat.html', {'form': form})  # Corrected 'post_create.html' here

def test_create(request):
    if request.method == 'POST':
        form = Test(request.POST)
        if form.is_valid():
            Post.objects.create(**form.cleaned_data)
        return HttpResponseRedirect('/posts/')
    else:
        form = Test()
        return render(request,'posts/post_test.html',{'context':form})

@api_view(['GET'])
def test(request):
    try:
        return Response(PostSerializer1(Post.objects.all(), many=True).data,status=status.HTTP_202_ACCEPTED)
    except Post.DoesNotExist:
        return Response({'eror':'this is post not found by paiman'},status=status.HTTP_100_CONTINUE)

@api_view(['GET'])
def test2(request):
    try:
        return Response(PostSerializer2(Post.objects.get(pk=20)).data, status=status.HTTP_202_ACCEPTED)
    except Post.DoesNotExist:
        return Response ({'paiman':'i did but that is error please go back and do it agani'},status=status.HTTP_400_BAD_REQUEST)
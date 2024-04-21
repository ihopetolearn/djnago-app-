"""
URL configuration for arif project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from posts.views import test, home, post_list,post_detail,post_create,test_create,index,test2

urlpatterns = [
    path('admin/', admin.site.urls),
    path('test/', test,name = 'seriaizer'),
    path('home/', home),
    path('posts/', post_list),  # Update the URL pattern for post list view
    path('posts/<int:pk>/',post_detail),  # Update the URL pattern for post detail view
    path('post/',post_create),
    path('post/create/',test_create),
    path('api-auth/', include('rest_framework.urls')),
    path('index/',index, name= 'serializer2'),
    path('test2/',test2, name='one serializer')


]
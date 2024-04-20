from django.db import models


class post(models.Model):
    title= models.CharField(max_length=10)
    text= models.TextField(max_length=500, blank=True)
    is_enabled= models.BooleanField(default=True)
    email = models.EmailField(null=True)
    image = models.ImageField(upload_to="static/images",null=True)


    objects = models.manager

    def __str__(self):
        return '{},{}'.format(self.id,self.title)


class comment(models.Model):
    post = models.ForeignKey(post,on_delete=models.CASCADE)
    title = models.TextField(post,max_length=20,null=True)
    text = models.TextField(max_length=200,null=True,blank=True)
    start_time = models.DateTimeField(null=True)


# Create your models here.

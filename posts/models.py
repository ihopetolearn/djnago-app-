from django.db import models

class post(models.Model):
    title= models.CharField(max_length=10)
    text= models.TextField(max_length=500, blank=True)
    is_enabled= models.BooleanField(default=True)
    published_date = models.DateField()
    created_date = models.DateField()
    updated_date = models.DateTimeField(auto_now=False)

# Create your models here.

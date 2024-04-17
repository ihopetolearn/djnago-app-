from django.db import models

class post(models.Model):
    title= models.CharField(max_length=10)
    text= models.CharField(max_length=50)
    is_enabled= models.BooleanField(default=True)
    published_date = models.DateField()
    created_date = models.DateField()
    updated_date = models.DateTimeField()

# Create your models here.

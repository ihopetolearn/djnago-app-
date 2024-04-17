from django.contrib import admin
from .models import post

class postadmin(admin.ModelAdmin):
    list_display = ('title','is_enabled','published_date','created_date','updated_date')

admin.site.register(post,postadmin)
# Register your models here.

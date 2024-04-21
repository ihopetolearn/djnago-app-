from django.contrib import admin
from .models import Post,comment

class commentinline(admin.TabularInline):
    model = comment
    fields = ['text','start_time']
    extra = 0
@admin.register(Post)
class postadmin(admin.ModelAdmin):
    list_display = ('id','title','is_enabled')
    inlines = [commentinline]

# admin.site.register(post,postadmin)
# admin.site.register(comment,commentadmin)
# Register your models here.

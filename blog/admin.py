from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):
    model = Post
    list_display = ('title','category','created','status','language')
    list_filter=['status', 'category','language']
    search_fields=['title','content','permission_text']
    filter_horizontal = ('tags',)

admin.site.register(Post, PostAdmin)
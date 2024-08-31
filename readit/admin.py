from django.contrib import admin
from .models import Post, Comment, Board

class PostAdmin(admin.ModelAdmin):
        model = Post

admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
admin.site.register(Board)
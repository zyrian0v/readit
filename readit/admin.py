from django.contrib import admin
from .models import Post, Comment, Board, Vote

class PostAdmin(admin.ModelAdmin):
        model = Post

admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
admin.site.register(Board)
admin.site.register(Vote)
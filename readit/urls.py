from django.urls import path
from . import views

urlpatterns = [
        path("", views.index, name="index"),
        path("comment/<int:comment_id>/delete", views.delete_comment, name="delete_comment"),
        path("<slug:board_name>/<int:post_id>", views.post, name="post"),
        path("<slug:board_name>/<int:post_id>/new_comment", views.new_comment, name="new_comment"),
        path("<slug:board_name>/<int:post_id>/delete", views.delete_post, name="delete_post"),
        path("<slug:board_name>/new", views.new_post, name="new_post"),
        path("profile/<username>", views.profile, name="profile"),
        path("register", views.register, name="register"),
        path("<slug:name>", views.board, name="board"),
]
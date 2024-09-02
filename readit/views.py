from django.conf import settings
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment, Board, Vote
from .forms import PostForm, RegistrationForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponse

def index(request):
        posts = Post.objects.all()
        return render(request, "readit/index.html", {
                "posts": posts,
        })


def board(request, name):
        board = get_object_or_404(Board, name=name)
        posts = board.post_set.all()
        
        return render(request, "readit/board.html", {
                "board": board,
                "posts": posts,
        })

def post(request, board_name, post_id):
        post = get_object_or_404(Post, pk=post_id)
        comments = post.comment_set.filter(parent=None)
        return render(request, "readit/post.html", {
                "post": post,
                "comments": comments,
        })

def new_post(request, board_name):
        if not request.user.is_authenticated:
                return redirect(f"{settings.LOGIN_URL}?next={request.path}")

        if request.method == "POST":
                form = PostForm(request.POST)
                if form.is_valid():
                        title = form.cleaned_data["title"]
                        url = form.cleaned_data["url"]
                        description = form.cleaned_data["description"]
                        board = Board.objects.get(name=board_name)

                        post = Post(title=title, url=url, description=description, board=board)
                        post.user = request.user
                        post.save()
                        return redirect("board", name=board_name)
        
        form = PostForm()
        return render(request, "readit/new_post.html", {
                "form": form,
                "board_name": board_name,
        })

def new_comment(request, board_name, post_id):
        if not request.user.is_authenticated:
                return redirect(f"{settings.LOGIN_URL}?next={request.path}")

        if request.method == "POST":
                parent_id = request.POST.get("parent_id")
                content = request.POST["comment"]
                comment = Comment(content=content, post_id=post_id, user=request.user, parent_id=parent_id)
                comment.save()
                return redirect("post", board_name=board_name, post_id=post_id)
                
        return redirect("index")

def profile(request, username):
        profile = get_object_or_404(User, username=username)
        posts = profile.post_set.all()
        comments = profile.comment_set.all()
        is_you = request.user == profile
        return render(request, "readit/profile.html", {
                "profile": profile,
                "posts": posts,
                "comments": comments,
                "is_you": is_you,
        })

def register(request):
        if request.method == "POST":
                form = RegistrationForm(request.POST)

                if form.is_valid():
                        username = form.cleaned_data["username"]
                        password = form.cleaned_data["password"]
                        password2 = form.cleaned_data["password2"]

                        if password != password2:
                                messages.error(request, "Passwords don't match.")
                                return redirect("register")
                        
                        if User.objects.filter(username=username).first():
                                messages.error(request, "Username already exists.")
                                return redirect("register")
                        
                        user = User.objects.create_user(username=username, password=password)
                        user.save()
                        return redirect("login")

        form = RegistrationForm()
        return render(request, "readit/register.html", {
                "form": form,
        })

def delete_post(request, board_name, post_id):
        if request.method == "POST":
                post = Post.objects.get(id=post_id)
                if request.user == post.user:
                        post.delete()
        return redirect("profile", username=request.user.username)

def delete_comment(request, comment_id):
        if request.method == "POST":
                comment = Comment.objects.get(id=comment_id)
                if request.user == comment.user:
                        comment.delete()
        return redirect("profile", username=request.user.username)

def upvote(request, post_id):
        if request.method == "POST":
                vote = Vote.objects.filter(post_id=post_id, user=request.user).first()
                if not vote:
                        post = Post.objects.get(id=post_id)
                        post.votes += 1
                        post.save()
                        new_vote = Vote(post_id=post_id, user=request.user, vote=Vote.DOWNVOTE)
                        new_vote.save()
                        return HttpResponse("upvoted in django")
                else:
                        return HttpResponse("already voted")
        return HttpResponse("wrong method")
        
def downvote(request, post_id):
        if request.method == "POST":
                vote = Vote.objects.filter(post_id=post_id, user=request.user).first()
                if not vote:
                        post = Post.objects.get(id=post_id)
                        post.votes -= 1
                        post.save()
                        new_vote = Vote(post_id=post_id, user=request.user, vote=Vote.DOWNVOTE)
                        new_vote.save()
                        return HttpResponse("downvoted in django")
                else:
                        return HttpResponse("already voted")
        return HttpResponse("wrong method")
        
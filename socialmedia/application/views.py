from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect
from core.models import Profile
from .forms import PostForm
from .models import Post
from django.contrib.auth.models import User
from django.contrib import messages
def home(request):
    if request.user.is_authenticated:
        liked = Post.objects.filter(likes=request.user)
        posts = Post.objects.all()
        return render(request, 'home.html', {'posts': posts, 'liked': liked})
    else:
        return redirect('login')

def dashboard(request):
    if request.user.is_authenticated:
        posts = Post.objects.filter(user=request.user).all()
        return render(request, 'app/dashboard.html', {'posts': posts})
    else:
        return redirect('login')

def upload_post(request):
    form = PostForm(request.POST or None, request.FILES)
    if request.user.is_authenticated:
        if request.method == 'POST':
            if form.is_valid():
                post = form.save(commit=False)
                post.user = request.user
                post.save()
                messages.success(request, "You post has been created successfully...")
                return redirect('home')
        else:
            return render(request, "app/upload_post.html", {"form": form})
    else:
        messages.error(request, "You must be logged in to perform this action!!!")
        return redirect('login')
    

@csrf_exempt
def like_post(request, post_id):
    if request.method == "POST":
        post = Post.objects.get(id=post_id)
        if request.user in post.likes.all():
            post.likes.remove(request.user)
            liked = False
        else:
            post.likes.add(request.user)
            liked = True
        return JsonResponse({"success": True, "liked": liked, "likes_count": post.likes.count()})
    return JsonResponse({"success": False}, status=400)


@csrf_exempt
def like_post_one(request, title):
    if request.method == "POST":
        try:
            post = Post.objects.get(title=title)
            if request.user in post.likes.all():
                post.likes.remove(request.user)
                liked = False
            else:
                post.likes.add(request.user)
                liked = True
            return JsonResponse({"success": True, "liked": liked, "likes_count": post.likes.count()})
        except Post.DoesNotExist:
            return JsonResponse({"success": False, "error": "Post not found."}, status=404)
    return JsonResponse({"success": False}, status=400)

def delete_post(request, post_id):
    if request.user.is_authenticated:
        post = get_object_or_404(Post, id=post_id)
        
        if post.user == request.user:
            post.delete()
            messages.success(request, "Your post has been deleted.")
            return redirect('dashboard')
        else:
            messages.error(request, "You are not authorized to perform this action.")
            return redirect('home')
    else:
        messages.error(request, "You must be logged in to perform this action.")
        return redirect('login')

def update_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if post.user != request.user:
        messages.error(request, "You are not authorized to edit this post.")
        return redirect('home')
    
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        
        if form.is_valid():
            form.save()
            messages.success(request, "Your post has been updated successfully.")
            return redirect('dashboard')

        else:
            messages.error(request, "There was an error in your form. Please check the fields.")
    else:
        form = PostForm(instance=post)

    return render(request, 'app/update_post.html', {'form': form, 'post': post})

def user_posts(request, username):
    if request.user.is_authenticated:
        user = get_object_or_404(User, username=username)
        profile = get_object_or_404(Profile, user=user)
        posts = Post.objects.filter(user=user).order_by('-created_at')
        liked = Post.objects.filter(likes=request.user)

        return render(request, "app/user_posts.html", {"user": user, "posts": posts, "profile": profile, "liked": liked})
    else:
        messages.error(request, "You must be logged in to perform this action.")
        return redirect('login')
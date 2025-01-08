from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignupForm
from .models import Profile
from django.contrib.auth.models import User
def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            profile_image = form.cleaned_data.get('profile_image')
            bio = form.cleaned_data.get('bio')
            dob = form.cleaned_data.get('dob')

            Profile.objects.create(user=user, profile_image=profile_image, bio=bio, dob=dob)

            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                data = Profile.objects.filter(user=user).first()
                messages.success(request, "You signed up successfully!")
                return render(request, 'home.html', {"data": data})
            else:
                messages.error(request, "Authentication failed after signup.")
        else:
            messages.error(request, "Invalid signup details. Please correct the errors.")
    else:
        form = SignupForm()

    return render(request, 'auth_html/signup.html', {'form': form})

def logout_user(request):
    logout(request)
    return redirect('login')

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        #authenticate
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have been logged in!!!")
            return redirect('home')
        else:
            messages.error(request, "Oooops!!!🥴 An error occurred while logging in! Try again...")
            return redirect('login')
    else:
        return render(request, 'auth_html/login.html', {})
    

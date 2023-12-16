from django.core import mail
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth import logout
from .models import Post
from datetime import datetime, timedelta

def sign_up(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            expiry_date = datetime.now() + timedelta(days=7)
            response = redirect('home')
            response.set_cookie('username', username, expires=expiry_date)
            return response
        else:
            messages.error(request, 'Unsuccessful registration. Invalid information.')
    if request.user.is_authenticated:
            return redirect('home')

    return render(request, "login.html")


def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        subject = "Thank you for the registration"
        message = 'Have a fun time reading our blog'
        recipient_list = [email]
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')
        if User.objects.filter(username=username).exists():
            messages.error(request, "This username is already taken")
            return redirect('home')

        if pass1 != pass2 and username==pass1:
            messages.error(request, 'Unsuccessful registration. Invalid information.')
        else:
            my_user = User.objects.create_user(username, email, pass1)
            my_user.save()
            try:
                send_mail(subject, message, settings.EMAIL_HOST_USER, recipient_list, fail_silently=True)
                print('email sent')
                return redirect('login')
            except Exception as e:
                print('An error occurred while sending the message:', str(e))

    return render(request, 'register.html')


def home(request):
    return render(request, 'index.html')

def retreat(request):
    return render (request, 'index.html')


def inventory(request):
    return render (request, 'inventory.html')

def post(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'post.html', context)

def logout_user(request):
    logout(request)
    return redirect ('login')


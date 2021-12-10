from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from .forms import NewUSerForm
import re
from django.conf import settings
from django.core.mail import send_mail

def signup_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if(re.fullmatch(regex, email)):
            form = NewUSerForm(request.POST)
            if form.is_valid():
                user = form.save()
                subject = 'welcome to UrbanEats'
                message = f'Hi {user.username}, thank you for signing up on UrbanEats.'
                email_from = settings.EMAIL_HOST_USER
                recipient_list = [user.email, ]
                send_mail( subject, message, email_from, recipient_list )
                login(request, user)
                return redirect('main:home')
            else:
                form = NewUSerForm()
    else:
        form = NewUSerForm()
    return render(request, 'accounts/signup.html', { 'form': form })

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            return redirect('main:home')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', { 'form': form })

def logout_view(request):
    if request.method == 'POST':
            logout(request)
            return redirect('/')
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import RegisterForm
from .models import Category, Course, Student


def RegisterView(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST, request.FILES)

        if form.is_valid():
            user_data = form.save(commit=False)
            user_data.set_password(form.cleaned_data['password'])
            user_data.save()

            Student.objects.get_or_create(name=user_data.username)

            return redirect('login')
    else:
        form = RegisterForm()

    return render(request, 'register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        login_input = request.POST.get('username', '').strip()
        password = request.POST.get('password')

        # Check if the user entered an email address instead of a username
        if '@' in login_input:
            user_obj = User.objects.filter(email=login_input).first()
            username = user_obj.username if user_obj else login_input
        else:
            username = login_input

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('success')
        else:
            messages.error(request, 'Invalid username or password.')

    return render(request, 'login.html')


@login_required(login_url='login')
def success_view(request):
    all_courses = Course.objects.filter(is_published=True)
    all_categories = Category.objects.all()

    context = {
        'courses': all_courses,
        'categories': all_categories,
    }
    return render(request, 'success.html', context)


def logout_view(request):
    auth_logout(request)
    messages.success(request, 'You have successfully logged out.')
    return redirect('login')

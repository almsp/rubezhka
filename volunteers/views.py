from volunteers.models import Volunteers
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


def volunteers(request):
    volunteers = Volunteers.objects.all()
    return render(request, "volunteers.html", context={"volunteers": volunteers})


def user_login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(username=email, password=password)
        if user is not None:
            print(user, 1)
            login(request, user)
            return redirect('animals')
        else:
            print(user, 2)
            return render(request, 'login.html', {'error': 'Invalid username or password'})
    else:
        return render(request, 'login.html')


def user_logout(request):
    logout(request)
    return redirect('animals')


def register(request):
    if request.method == 'POST':
        email = request.POST.get('email', '')
        password = request.POST.get('password', '')
        if not User.objects.filter(username=email).exists():
            user = User.objects.create_user(username=email, email=email, password=password)
            user = authenticate(request, username=email, password=password)
            user.save()
            login(request, user)
            return redirect('animals')
        else:
            return redirect('register')
 
    else:
        return render(request, 'register.html')
    


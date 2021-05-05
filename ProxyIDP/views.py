from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.models import User


# Create your views here.

def my_view(request):
    name = "user1"
    pwd = "123"
    user = User.objects.create_user(name, 'user1@p.com', pwd)

    # At this point, user is a User object that has already been saved
    # to the database. You can continue to change its attributes
    # if you want to change other fields.
    user.save()

    user = authenticate(request, username=name, password=pwd)
    if user is not None:
        login(request, user)
        print("Login Successful")
        return redirect(request.GET.get('next'))
    else:
        print("Login Failure")

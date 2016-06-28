from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from login import settings
from django.contrib.auth.decorators import login_required

def Login(request):
    next = request.GET.get('next', '/blog/')


    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect(next)

        else:
            return HttpResponseRedirect(settings.LOGIN_URL)

    return render(request, "index/login.html", {'redirect_to': next})

def Logout(request):
    logout(request)
    return HttpResponseRedirect(settings.LOGIN_URL)

@login_required

def Blog(request):
    return render(request, "index/blog.html", {})
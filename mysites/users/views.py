from django.shortcuts import render, redirect
from django.core.context_processors import csrf
from django.contrib.auth import *


# Create your views here.
def user_login(request):
    """
    login
    """
    if request.POST:
        username = password = ''
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None and user.is_active:
            login(request, user)
            return redirect('/')

    ctx = {}
    ctx.update(csrf(request))
    return render(request, 'user_login.html',ctx)

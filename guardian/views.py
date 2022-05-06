from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from guardian.forms import UserForm
from django.contrib.auth.models import Group
from core.models import Person


# Create your views here.


def registerpage(request):
    form = UserForm
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            group = Group.objects.get(id=4)
            user.groups.add(group)
            person = Person.objects.create(
                user=user,
                type=group.name
            )
            person.save()
            return redirect('LoginPage')
    return render(request, 'register.html', context={'form': form})


def loginpage(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request,data=request.POST)
        if form.is_valid():
            uname = form.cleaned_data['username']
            upass = form.cleaned_data['password']
            user = authenticate(username=uname, password=upass)
            if user is not None:
                login(request, user)
                return redirect('HomePage')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', context={'form': form})


def logoutpage(request):
    logout(request)
    return redirect('HomePage')

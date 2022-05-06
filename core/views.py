from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# Create your views here.

def is_expired(user):
    return user.groups.filter(id=2).exists()


@login_required(login_url='LoginPage')
def homepage(request):
    if is_expired(request.user):
        return HttpResponse("Expired<a href='/guardian/logout/'>Logout</a>")
    else:
        return HttpResponse("HomePage<a href='/guardian/logout/'>Logout</a>")

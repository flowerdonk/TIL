from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm


def stw(request):
    form = AuthenticationForm()
    context = {
        'form' : form
    }
    return render(request, 'members/stw.html', context)

def kbh(request):
    form = AuthenticationForm()
    context = {
        'form' : form
    }
    return render(request, 'members/kbh.html', context)
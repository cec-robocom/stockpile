from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm


def index(request):
    context = {}
    return render(request, 'library/index.html', context)


def register(request):
    form = UserCreationForm()
    context = {"form": form }
    print(form)
    return render(request, 'registration/register.html', context)
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, "index.html")


def login(request):
    return render(request, "login.html")

from http.client import HTTPResponse

from django.http import HttpResponse
from django.shortcuts import render

def Home(request):
    return render(request, 'index.html')


def Login(request):
    return render(request, "login.html")


def About(request):
    return render(request, "about.html")


def Contact(request):
    return render(request, "contact.html")

def Signup(request):
    return render(request, "Register.html")


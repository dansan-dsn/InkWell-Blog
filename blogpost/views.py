# from django.http import HttpResponse
from django.shortcuts import render, redirect
from users.models import User


def homepage(request):
    return render(request, 'index.html')
    
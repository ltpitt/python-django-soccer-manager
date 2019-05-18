from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    return HttpResponse("Welcome to Soccer Manager Teams page <a href=\"/accounts/logout\">Logout</a>")

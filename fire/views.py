from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from requests import request
import json
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.conf import settings


def index(request):
    return render(request,'index.html')

def login_firebase(request):
    return render(request,"login_firebase.html")

@login_required
def home(request):
    return render(request,'home.html')

def LoginView(request):
    return render(request,'login.html')




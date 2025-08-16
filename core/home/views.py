from django.shortcuts import render , redirect
from .models import Recipe
from django.http import HttpResponse , JsonResponse , HttpResponseRedirect
from django.contrib import messages 
from django.contrib.auth import login , authenticate , logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

def home(request):

    return render(request , 'home/index.html' , context={})

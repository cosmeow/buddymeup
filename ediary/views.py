from django import template
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader

from .models import ExerciseLocation, Users, Exercise, Activities

# Create your views here.
def index(request):
    return render(request, 'ediary/index.html')

def register(request):
    return render(request, 'ediary/register.html')

def home(request, users_id):
    user = get_object_or_404(Users, pk=users_id)
    return render(request, 'ediary/home.html', {'user': user, 'elocation': ExerciseLocation})
    
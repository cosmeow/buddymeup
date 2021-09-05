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

#def get_queryset(ExerciseLocation):
#    return ExerciseLocation.objects.order_by('-location')[:5]   

def home(request, users_id): 
    user = get_object_or_404(Users, pk=users_id)
    elocation = get_object_or_404(ExerciseLocation, pk=1)
#    return render(request, 'ediary/home.html', {'user': user, 'elocation': get_queryset(ExerciseLocation)})
    return render(request, 'ediary/home.html', {'user': user, 'elocation': elocation})
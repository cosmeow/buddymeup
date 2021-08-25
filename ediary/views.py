from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import ExerciseLocation, Users, Exercise, Activities

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the exercise diary index.")


def home(request, users_id):
    user = get_object_or_404(Users, pk=users_id)
    return HttpResponse("Hello {}".format(Users.first_name))
    
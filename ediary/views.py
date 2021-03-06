from django import template
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.template import loader
from .forms import PostRegistrationForm, PostActivityForm

from .models import ExerciseLocation, Users, Exercise, Activities

# Create your views here.
def index(request):
    return render(request, 'ediary/index.html')

def users_new(request):
    if request.method == "POST":
      form = PostRegistrationForm(request.POST)
      if form.is_valid():
          users = form.save(commit=True)
          return redirect('ediary:users_reg_success', pk=users.pk)
    else:
        form = PostRegistrationForm()
    return render(request, 'ediary/users_edit.html', {'form': form})

def users_reg_success(request, pk):
    user = get_object_or_404(Users, pk=pk)
    return render(request, 'ediary/users_reg_success.html', {'users': user})

def users_edit(request, pk):
    user = get_object_or_404(Users, pk=pk)
    if request.method == "POST":
        form = PostRegistrationForm(request.POST, instance=user)
        if form.is_valid():
            user = form.save(commit=True)
            return redirect('users_detail', pk=user.pk)
        else:
            form = PostRegistrationForm(instance=user)
        return render(request, 'ediary/users_edit.html', {'form': form})
# def register(request):
#     print(request.POST)
#     return render(request, 'ediary/register.html')

def home(request, users_id):
    user = get_object_or_404(Users, pk=users_id)
    elocation = ExerciseLocation.objects.all()
    exercises = Exercise.objects.all()
    activitylog = Activities.objects.filter(user_id=users_id)
    context = {
        'user': user,
        'elocation': elocation,
        'exercises': exercises,
        'activitylog': activitylog,
    }
    return render(request, 'ediary/home.html', context)

def new_activity(request):
    if request.method == "POST":
        form = PostActivityForm(request.POST)
        if form.is_valid():
            activity = form.save(commit=True)
            return render(request, 'ediary/new_activity.html', {'form': form}) 
    else:
        form = PostActivityForm()
    return render(request, 'ediary/new_activity.html', {'form': form})    
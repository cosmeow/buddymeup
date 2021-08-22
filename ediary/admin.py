from django.contrib import admin

from .models import ExerciseType, ExerciseLocation

# Register your models here.
admin.site.register(ExerciseType)
admin.site.register(ExerciseLocation)
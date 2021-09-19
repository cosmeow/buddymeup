from django.contrib import admin

from .models import ExerciseLocation
from .models import Users
from .models import Exercise
from .models import Activities
# Register your models here.
admin.site.register(Users)
admin.site.register(ExerciseLocation)
admin.site.register(Exercise)
admin.site.register(Activities)

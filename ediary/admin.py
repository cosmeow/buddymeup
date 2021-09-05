from django.contrib import admin

from .models import ExerciseLocation
from .models import Users
# Register your models here.
admin.site.register(ExerciseLocation)
admin.site.register(Users)
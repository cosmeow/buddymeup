import datetime

from django.db import models
from django.utils import timezone

# Create your models here.
class ExerciseLocation(models.Model):
    location = models.CharField(max_length=500)
    def __str__(self):
        return self.location

class ExerciseType(models.Model):
    exercise_type = models.CharField(max_length=500)
    def __str__(self):
        return self.exercise_type

class ExerciseDiary(models.Model):
    location = models.ForeignKey(ExerciseLocation, on_delete=models.CASCADE)
    exercise_type = models.ForeignKey(ExerciseType, on_delete=models.CASCADE)
    exercise_date = models.DateTimeField('date exercised')

    def exercised_recently(self):
        return self.exercise_date >= timezone.now() - datetime.timedelta(days=1)

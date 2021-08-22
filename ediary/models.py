import datetime

from django.db import models
from django.db.models.fields import IntegerField
from django.utils import timezone

# Create your models here.
class ExerciseLocation(models.Model):
    location = models.CharField(max_length=500)
    def __str__(self):
        return self.location

class ExerciseType(models.Model):
    type = models.CharField(max_length=500)
    def __str__(self):
        return self.type

class StrengthDiary(models.Model):
    type = models.ForeignKey(ExerciseType, on_delete=models.CASCADE)
    reps = IntegerField()
    sets = IntegerField()
    strength_date = models.DateTimeField('strength exercise date')

    def strength_exercise_recently(self):
        return self.strength_date >= timezone.now() - datetime.timedelta(days=1)

class CardioDiary(models.Model):
    location = models.ForeignKey(ExerciseLocation, on_delete=models.CASCADE)
    type = models.ForeignKey(ExerciseType, on_delete=models.CASCADE)
    cardio_date = models.DateTimeField('cardio exercise date')

    def cardio_exercise_recently(self):
        return self.cardio_date >= timezone.now() - datetime.timedelta(days=1)

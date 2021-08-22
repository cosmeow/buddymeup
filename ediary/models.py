import datetime

from django.db import models
from django.db.models.fields import IntegerField
from django.utils import timezone

# Create your models here.
class ExerciseLocation(models.Model):
    location = models.CharField(max_length=500)
    IN = 'IN'
    OUT = 'OUT'
    LOCATION_TYPE_CHOICES = (
                (IN, 'Indoor'),
                (OUT, 'Outdoor'),
            )
    location_type = models.CharField(max_length = 3, choices = LOCATION_TYPE_CHOICES, default = IN)
    def __str__(self):
        return self.location

class Users(models.Model):
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 100)
    email = models.EmailField(max_length = 254)
    password = models.CharField(max_length = 10)
    

class Exercise(models.Model):
    C = 'C'
    S = 'S'
    CATEGORY_CHOICES = [
                    (C, 'Cardio'),
                    (S, 'Strength'),
                ]
    category = models.CharField(max_length = 1, choices = CATEGORY_CHOICES, default = C)

    RUN = 'RUN'
    SWIM = 'SWIM'
    WALK = 'WALK'
    CYCLE = 'CYCLE'
    EXERCISE_CHOICES = (
            (RUN, 'Run'),
            (SWIM, 'Swim'),
            (WALK, 'Walk'),
            (CYCLE, 'Cycle'),
        )
    exercise_name = models.CharField(max_length = 5, choices = EXERCISE_CHOICES, default = RUN)
    

class Activities(models.Model):
    user = models.ForeignKey(Users, on_delete = models.CASCADE)
    location = models.ForeignKey(ExerciseLocation, on_delete = models.CASCADE)
    exercise = models.ForeignKey(Exercise, on_delete = models.CASCADE)
    date = models.DateTimeField()
    duration_hrs = models.PositiveIntegerField()
    duration_min = models.PositiveIntegerField()
    duration_sec = models.PositiveIntegerField()
    distance_km = models.PositiveIntegerField(default = 0)
    def cardio_exercise_recently(self):
        return self.date >= timezone.now() - datetime.timedelta(days=1)
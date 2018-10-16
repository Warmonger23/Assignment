from django.db import models


# Create your models here.

class leaderBoard(models.Model):
    teamName = models.CharField(max_length=100, default='null')
    games_played = models.IntegerField(default=0)
    wins = models.IntegerField(default=0)
    draws = models.IntegerField(default=0)
    loss = models.IntegerField(default=0)
    goals_for = models.IntegerField(default=0)
    goals_against = models.IntegerField(default=0)
    goals_difference = models.IntegerField(default=0)
    points = models.IntegerField(default=0)

    def __str__(self):
        return self.teamName

from django.db import models

class Stadium(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Team(models.Model):
    name = models.CharField(max_length=200)
    stadium_id = models.ManyToManyField(Stadium, through='StadiumTeam')
    def __str__(self):
        return self.name

class StadiumTeam(models.Model):
    stadium_id = models.ForeignKey(Stadium,on_delete = models.CASCADE)
    team_id = models.ForeignKey(Team,on_delete = models.CASCADE)
    class Meta:
        db_table = 'has_stadium'

class Position(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Player(models.Model):
    name = models.CharField(max_length=200)
    position_id = models.ForeignKey(Position,on_delete = models.CASCADE)
    number = models.IntegerField()
    team_id = models.ForeignKey(Team,on_delete = models.CASCADE)
    def __str__(self):
        return self.name
from django.db import models
class User(models.Model):
    id = models.AutoField(primary_key='True')
    username = models.CharField(max_length=25,unique='True',blank='False')
    password = models.CharField(max_length=25, blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True,default='user_default')
    dob = models.CharField(max_length=20, blank=True, null=True)
    weight = models.FloatField(blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    sport = models.CharField(max_length=30, blank=True, null=True)
    phone = models.BigIntegerField(blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=25, blank=True, null=True)
    image = models.CharField(max_length=100, blank=True, null=True)
    account_number = models.CharField(max_length=20, blank=True, null=True)
    ifsc_code = models.CharField(max_length=11, blank=True, null=True)

    class Meta:
        db_table = 'user'

    
class Event(models.Model):
    id = models.AutoField(primary_key='True')
    event_name = models.CharField(max_length=50, blank=True, null=True)
    event_game = models.CharField(max_length=250, blank=True, null=True)
    event_logo = models.CharField(max_length=30, blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    organiser = models.ForeignKey('User', on_delete=models.CASCADE,null=True)
    event_start = models.DateTimeField(blank=True, null=True)
    event_end = models.DateTimeField(blank=True, null=True)
    description = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        db_table = 'event'


class Tournament(models.Model):
    id = models.AutoField(primary_key='True')
    tournament_name = models.CharField(max_length=100, blank=True, null=True)
    game = models.CharField(max_length=30, blank=True, null=True)
    tournament_mode = models.CharField(max_length=10, blank=True, null=True)
    tournament_type = models.CharField(max_length=30, blank=True, null=True)
    event = models.ForeignKey(Event, on_delete=models.CASCADE,null=True)
    number_of_teams = models.IntegerField(blank=True, null=True)
    number_of_round = models.IntegerField(blank=True, null=True)
    number_of_matches = models.IntegerField(blank=True, null=True)
    tournament_image = models.CharField(max_length=100, blank=True, null=True)
    tournament_start = models.DateTimeField(blank=True, null=True)
    tournament_end = models.DateTimeField(blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    organiser = models.ForeignKey('User', on_delete=models.CASCADE,null=True)

    class Meta:
        db_table = 'tournament'


class Team(models.Model):
    id = models.AutoField(primary_key='True')
    team_name = models.CharField(max_length=30, blank=True, null=True)
    team_logo = models.CharField(max_length=100, blank=True, null=True)
    
    class Meta:
        db_table = 'team'


class TeamInformation(models.Model):
    id = models.AutoField(primary_key='True')
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    tournament = models.ForeignKey('Tournament', on_delete=models.CASCADE,null=True)
    player = models.ForeignKey('User', on_delete=models.CASCADE,null=True)
    
    class Meta:
        db_table = 'team_information'


class Summary(models.Model):
    id = models.AutoField(primary_key='True')
    event = models.ForeignKey(Event, on_delete=models.CASCADE,null=True)
    tournament = models.ForeignKey('Tournament', on_delete=models.CASCADE,null=True)
    winner_team = models.ForeignKey('Team', on_delete=models.CASCADE,null=True)
    class Meta:
        db_table = 'summary'

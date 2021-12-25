from django.db import models

# Create your models here.

class Availability(models.Model):
    id = models.IntegerField(primary_key=True)
    availdate = models.DateField(db_column='availDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'availability'

class Role(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=16, db_collation='utf8mb4_0900_ai_ci')

    def __str__(self) -> str:
        return "name="+self.name+"\nid="+str(self.id)

    class Meta:
        managed = False
        db_table = 'role'


class User(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=16)
    last_name = models.CharField(max_length=15)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=32)
    phone_num = models.IntegerField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    state = models.CharField(max_length=12)
    role = models.ForeignKey(Role, models.DO_NOTHING)
    availability = models.ForeignKey(Availability, models.DO_NOTHING)

    def __str__(self) -> str:
        return "name="+self.name+"\nemail="+self.email+"\nid="+str(self.id)

    class Meta:
        managed = False
        db_table = 'user'
        unique_together = (('id', 'availability'),)

class Task(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=16)
    description = models.CharField(max_length=2045, blank=True, null=True)
    start_date = models.DateField()

    class Meta:
        managed = False
        db_table = 'task'


class TaskHasTeam(models.Model):
    task = models.OneToOneField(Task, models.DO_NOTHING, primary_key=True)
    team_idteam = models.ForeignKey('Team', models.DO_NOTHING, db_column='team_idteam')

    class Meta:
        managed = False
        db_table = 'task_has_team'
        unique_together = (('task', 'team_idteam'),)


class TaskHasUser(models.Model):
    task = models.OneToOneField(Task, models.DO_NOTHING, primary_key=True)
    user = models.ForeignKey('User', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'task_has_user'
        unique_together = (('task', 'user'),)


class Team(models.Model):
    idteam = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45)
    description = models.CharField(max_length=2048)

    class Meta:
        managed = False
        db_table = 'team'

class UserHasTeam(models.Model):
    user = models.OneToOneField(User, models.DO_NOTHING, primary_key=True)
    team_idteam = models.ForeignKey(Team, models.DO_NOTHING, db_column='team_idteam')

    class Meta:
        managed = False
        db_table = 'user_has_team'
        unique_together = (('user', 'team_idteam'),)
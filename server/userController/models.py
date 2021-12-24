from django.db import models
from django.db.models.fields import CharField

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

""" class role(models.Model):
    id = models.IntegerField(primary_key=True)
    name = CharField(max_length=16) """

class User(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=16)
    last_name = models.CharField(max_length=15)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=32)
    phone_num = models.IntegerField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    state = models.CharField(max_length=12)
    role = models.ForeignKey(Role, models.DO_NOTHING)
    availability = models.ForeignKey(Availability, models.DO_NOTHING)

    def __str__(self) -> str:
        return "name="+self.name+"\nemail="+self.email+"\nid="+self.id

    class Meta:
        managed = False
        db_table = 'user'
        unique_together = (('id', 'availability'),)

""" class user(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=16)
    last_name = models.CharField(max_length=15)
    email = models.EmailField(max_length=255)
    password = models.CharField(max_length=32)
    phone_num = models.IntegerField(default=0)
    create_time = models.TimeField(auto_now_add=True)
    state = models.PositiveSmallIntegerField(default=1)
    # role 0 = Administrador
    role_id = models.ForeignKey(role,on_delete=models.SET_NULL,null=True) """



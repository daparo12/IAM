from typing import cast
from django.core import serializers
from django.contrib.auth.hashers import make_password, check_password
from django.db.utils import IntegrityError
from django.http.request import HttpRequest
from django.utils.dateparse import parse_date
from django.db import transaction
from django.db.models.base import Model
from django.db.models.fields import NullBooleanField, json
from django.http import HttpResponse, HttpResponseRedirect
from django.core.checks.messages import Error
from django.shortcuts import get_object_or_404,render
from django.http import JsonResponse
from .models import Availability, Role, Task, User, TaskHasUser

# Create your views here.

def addUser(request):
    exito=False
    try:
        if request.method == "POST":
            #password=make_password(request.POST['password'])
            user = User(id=request.POST['id'],name=request.POST['name'],last_name=request.POST['last_name'],email=request.POST['email'],password=request.POST['password'],phone_num=request.POST['phone_num'],state=1,role=2,Availability=0)
            user.save()
            exito=True
    except Exception:
        pass
    return JsonResponse({'status':exito})

def addAdmin(request):
    exito=False
    try:
        if request.method == "POST":
            #password=make_password(request.POST['password'])
            user = User(id=request.POST['id'],name=request.POST['name'],last_name=request.POST['last_name'],email=request.POST['email'],password=request.POST['password'],phone_num=request.POST['phone_num'],state=1,role=1,Availability=0)
            user.save()
            exito=True
    except Exception:
        pass
    return JsonResponse({'status':exito})

def addTask(request:HttpRequest):
    exito=False
    try:
        if request.method == "POST":
            with transaction.atomic():
                task = Task(name=request.POST['name'],description=request.POST['description'],start_date=parse_date(request.POST['start_date']))
                task.save()
                user = User.objects.get(pk=request.POST['id_user'])
                users = request.POST.getlist('users')
                if users:
                    for id in users:
                        usuario=User.objects.get(pk=id)
                        taskHasUser = TaskHasUser(task=task,user=usuario)
                        taskHasUser.save()
            exito=True
    except Exception:
        pass
    return JsonResponse({'status':exito})
    

def authUser(request):
    autenticado=False
    id=-1
    role_name=''
    try:
        user:User = User.objects.get(email=request.POST['email'])
        if request.POST['password'] == user.password:
            autenticado=True
            id=user.id
            role_name=(Role.objects.get(id=user.role)).name
    except (Model.DoesNotExist,Model.MultipleObjectsReturned):
        pass

    return JsonResponse({'status':autenticado,'id':id, 'role':role_name})

@transaction.atomic
def getUserInfo(request:HttpRequest):
    exito=False
    datos=''
    try:
        if request.methos == 'GET':
            user=User.objects.get(pk=request.GET['id'])
            datos = serializers.serialize("json",user)
            exito= True
    except  IntegrityError:
        pass
    return JsonResponse({'status':exito,'datos':datos})


def roleExist(request,role_id):
    existe=False
    try:
        role = Role.objects.get(pk=role_id)
        existe=True
    except Role.DoesNotExist:
        pass
    return JsonResponse({'status':existe})

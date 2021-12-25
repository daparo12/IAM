from django.urls import path

from . import views

urlpatterns = [
    path('checkRole/<int:role_id>/', views.roleExist, name='roleExist'),
    path('addUser/',views.addUser, name='addUser'),
    path('authUser/',views.authUser,name='authUser'),
    path('addTask/',views.addTask,name='addTask'),
    path('addAdmin/',views.addAdmin,name='addAdmin'),
    path('getUserInfo/',views.getUserInfo,name='getUserInfo')
]
from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
   path('',login,name='login'),
   path('superuser_login', superuser_login, name='superuser_login'),
   path('superuser_logout', superuser_logout, name='superuser_logout'),

   path('dashboard/',dashboard,name='dashboard'),
   path('dashboard1/',dashboard1,name='dashboard1'),
   path('view_Info/<int:pk>/',view_Info,name='view_Info'),

   path('dashboard3',dashboard3,name='dashboard3'),
   path('view_Info1/<int:pk>/',view_Info1,name='view_Info1'),

   path('accept/<int:pk>/',accept,name="accept"),
   path('view_Info1/<int:pk>/accept/', accept, name='accept'),
   path('viwe_Info1/<int:pk>/reject/', reject, name='reject'),

   path('internship/',internship,name='internship'),
   path('intern_applied/',intern_applied,name='intern_applied'),
   path('intern_info/<int:pk>/',intern_info,name='intern_info'),
   
   # path('select/<int:pk>/',select,name="select"),
   # path('intern_Info1/<int:pk>/select/', select, name='select'),
   # path('intern_Info1/<int:pk>/reject/', reject, name='reject'),



]
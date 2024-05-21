from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
   path('',login,name='login'),
   path('superuser_login', superuser_login, name='superuser_login'),
   path('superuser_logout', superuser_logout, name='superuser_logout'),

# --------------------- Dashboard ----------------------------
   path('dashboard/',dashboard,name='dashboard'),
   path('dashboard1/',dashboard1,name='dashboard1'),
   path('view_Info1/<int:pk>/',view_Info1,name='view_Info1'),

   path('dashboard2/',dashboard2,name='dashboard2'),
   path('view_Info2/<int:pk>/',view_Info2,name='view_Info2'),

   path('dashboard3/',dashboard3,name='dashboard3'),
   path('view_Info3/<int:pk>/',view_Info3,name='view_Info3'),

   path('dashboard4/',dashboard4,name='dashboard4'),
   path('view_Info4/<int:pk>/',view_Info4,name='view_Info4'),

   path('accept/<int:pk>/',accept,name="accept"),
   path('viwe_Info1/<int:pk>/', reject, name='reject'),

# --------------------- Internship ----------------------------
   path('internship/',internship,name='internship'),
   path('intern_applied/',intern_applied,name='intern_applied'),
   path('intern_info/<int:pk>/',intern_info,name='intern_info'),

   path('Select_intern/<int:pk>/',Select_intern,name="Select_intern"),
   path('Reject_intern/<int:pk>/', Reject_intern, name='Reject_intern'),
   
# --------------------- Mentoreship ----------------------------
   path('Mentoreship/',Mentoreship,name='Mentoreship'),
   path('Mentor_dash1/',Mentor_dash1,name='Mentor_dash1'),
   path('mentor_info1/<int:pk>/',mentor_info1,name='mentor_info1'),

   path('Mentor_dash2/',Mentor_dash2,name='Mentor_dash2'),
   path('mentor_info2/<int:pk>/',mentor_info2,name='mentor_info2'),

   path('Select/<int:pk>/',Select,name="Select"),
   path('Reject/<int:pk>/', Reject, name='Reject'),


#-------------------Corporate Training ------------------------
   path('corporate_training/',corporate_training,name='corporate_training'),
   path('corporate_dash1/',corporate_dash1,name='corporate_dash1'),
   path('corporate_info1/<int:pk>/',corporate_info1,name='corporate_info1'),


   path('Corporate_Select/<int:pk>/',Corporate_Select,name="Corporate_Select"),
   path('Corporate_Reject/<int:pk>/', Corporate_Reject, name='Corporate_Reject'),


#------------------- Fresher Training ------------------------
   path('fresher/',fresher,name='fresher'),
   # path('fresher_dash1/',fresher_dash1,name='fresher_dash1'),
   # path('fresher_info1/<int:pk>/',fresher_info1,name='fresher_info1'),


   # path('fresher_Select/<int:pk>/',fresher_Select,name="fresher_Select"),
   # path('fresher_Reject/<int:pk>/', fresher_Reject, name='fresher_Reject'),


]
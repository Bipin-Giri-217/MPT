import imp
from django.urls import path

from . import views


urlpatterns = [
     path('studentdashboard/<str:pk>', views.student, name= 'student'),
     path('studentMeeting', views.studentMeeting, name='student-meeting'),    
]

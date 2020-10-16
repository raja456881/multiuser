from django.urls import path
from . import views
urlpatterns = [
    
     path('',views.trainerProfile, name = 'trainer_profile'),
     path('addCourse',views.addCourse1, name = 'add_course'),
     path('students',views.students, name = 'students'),
     path('courses',views.trainerCourses, name = 'trainer_courses'),
     path("addcategory", views.addCategory, name="addcategory"),
     path("onlinecourse", views.onlineaddcourse, name="onlinecourse")

    
]
from django.urls import path
from . import views
urlpatterns = [
    path('homelogin/', views.homepage1 , name='homepage1'),
    path('', views.homePage , name='homePage'),
    path('course/<slug:slugfield>/',views.coursePage , name='course_page')
]

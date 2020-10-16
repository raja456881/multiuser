from django.urls import path
from . import views
urlpatterns = [
    #for courses

     path('',views.inventory, name = 'inventory'),
     path('add/',views.addCourse, name = 'add_Course'),
     path('edit/<slug:slugfield>',views.editCourse, name = 'edit_Course'),
     path('delete/<int:pk>',views.deleteCourse, name = 'delete_Course'),
     path('course',views.Course,name='course'),

     #for categories 

     path('add_category/',views.addCategory , name = 'add_category'),
     path('category/',views.showCategory , name = 'show_category'),
     path('edit_category/<slug:slugfield>',views.editCategory, name = 'edit_category'),
     path('delete_category/<int:pk>',views.deleteCategory, name = 'delete_category'),

     path('view/<slug:slugfield>', views.detailView, name='view_course'),

]
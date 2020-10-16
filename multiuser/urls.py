from django.urls import path
from . import views
urlpatterns = [

    path('regchoice/', views.Registerchoice, name='registerchoice'),
    path('stu_reg/', views.StudentSignUpView.as_view(), name='student_reg'),
    path('inst_reg/', views.InstituteSignUpView.as_view(), name='institute_reg'),
    path('fran_reg/', views.FranchiseSignUpView.as_view(), name='franchise_reg'),
    path('train_reg/', views.TrainerSignUpView.as_view(), name='trainer_reg'),
    path('admin_reg/', views.AdminView.as_view(), name='admin_reg'),
    path('login/', views.login, name='login'),
    path('logout',views.logoutPage,name='logout'),
    path('',views.user,name='user'),
    path('user_student', views.user_student, name='user_student'),
    path('user_trainer', views.user_trainer, name='user_trainer'),
    path('user_franchise', views.user_franchise, name='user_franchise'),


    # to display profile
    path('user_profile_student/<str:username>', views.studentProfile, name='u_student_Profile'),
    path('user_profile_trainer/<str:username>', views.trainerProfile, name='u_trainer_Profile'),
    path('user_profile_institute/<str:username>', views.instituteProfile, name='u_institute_Profile'),
    path('user_profile_franchise/<str:username>', views.franchiseProfile, name='u_franchise_Profile'),

    path('view/<slug:slugfield>', views.coursedetailView, name='multi_view_course'),

]


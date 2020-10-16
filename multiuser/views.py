from .models import *
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from multiuser.models import AdminProfile,FranchiseProfile,InstituteProfile,TrainerProfile, User
from student.models import Student
from inventory.models import CourseDetails
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from  django.contrib.auth.decorators import login_required
from  django.contrib.auth import authenticate, login, logout
from django.contrib.auth import login as auth_login
from django.views.generic import CreateView
from  .form import StudentSignUpForm,AdminSignUpForm,FranchiseSignUpForm,InstituteSignUpForm,TrainerSignUpForm
from .models import User


def Registerchoice(request):
    return render(request, 'register_choice.html')

class AdminView(CreateView):
    model = User
    form_class = AdminSignUpForm
    template_name = 'admin_reg.html'

    def form_valid(self, form):
        user = form.save()

        return redirect('login')



class TrainerSignUpView(CreateView):
    model = User
    form_class = TrainerSignUpForm
    template_name = 'trainer_reg.html'



    def form_valid(self, form):
        user = form.save()

        return redirect('login')

class StudentSignUpView(CreateView):
    model = User
    form_class = StudentSignUpForm
    template_name = 'student_reg.html'


    def form_valid(self, form):
        user = form.save()

        return redirect('login')

class InstituteSignUpView(CreateView):
    model = User
    form_class = InstituteSignUpForm
    template_name = 'institute_reg.html'


    def form_valid(self, form):
        user = form.save()

        return redirect('login')


class FranchiseSignUpView(CreateView):
    model = User
    form_class = FranchiseSignUpForm
    template_name = 'franchise_reg.html'


    def form_valid(self, form):
        user = form.save()

        return redirect('login')



'''Login page'''
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            type_obj = User.objects.get(username=user)
            auth_login(request, user)
            if user.is_authenticated and type_obj.is_admin:

               return redirect('course')
            elif user.is_authenticated and type_obj.is_franchise:

                return redirect('homepage1')

            elif user.is_authenticated and type_obj.is_institute:

                return redirect('homepage1')
            elif user.is_authenticated and type_obj.is_trainer:
                return redirect('homepage1')

            elif user.is_authenticated and type_obj.is_student:

                return redirect('homepage1')



        else:
            messages1=True
            return  render(request, "admin_login.html", {"messages1":messages1})


    return render(request,'admin_login.html')



'''Logout Page '''
def logoutPage(request):
    logout (request)
    return redirect('homePage')



def user(request):
    '''institute'''
    '''count'''
    institute_count=InstituteProfile.objects.all().count()

    '''apply filter'''

    all_institute=InstituteProfile.objects.all()

    '''franchise'''
    '''count'''
    franchise_count=FranchiseProfile.objects.all().count()

    '''apply filter'''
    all_franchise=FranchiseProfile.objects.all()


    '''student'''

    student_count=Student.objects.all().count()


    '''trainer'''

    trainer_count = TrainerProfile.objects.all().count()

    context={

        'all_institute':all_institute,
        'trainer_count':trainer_count,
        'student_count':student_count,
        'franchise_count':franchise_count,
        'institute_count':institute_count,
        'user_count':student_count+trainer_count+franchise_count+institute_count
    }

    return render(request,'user.html',context)



def user_franchise(request):
    '''institute'''
    '''count'''
    institute_count = InstituteProfile.objects.all().count()

    '''franchise'''
    '''count'''
    franchise_count = FranchiseProfile.objects.all().count()

    '''apply filter'''
    all_franchise = FranchiseProfile.objects.all()

    '''student'''

    student_count = Student.objects.all().count()

    '''trainer'''

    trainer_count = TrainerProfile.objects.all().count()

    context = {

        'all_franchise': all_franchise,
        'trainer_count': trainer_count,
        'student_count': student_count,
        'franchise_count': franchise_count,
        'institute_count': institute_count,
        'user_count': student_count + trainer_count + franchise_count + institute_count
    }


    return render(request,'user_franchise.html',context)


def user_student(request):
    all_student=Student.objects.all()
    student_count = Student.objects.all()

    '''institute'''
    '''count'''
    institute_count = InstituteProfile.objects.all().count()

    '''franchise'''
    '''count'''
    franchise_count = FranchiseProfile.objects.all().count()

    '''apply filter'''
    all_franchise = FranchiseProfile.objects.all()

    '''student'''

    student_count = Student.objects.all().count()

    '''trainer'''

    trainer_count = TrainerProfile.objects.all().count()

    context = {

        'all_student': all_student,
        'trainer_count': trainer_count,
        'student_count': student_count,
        'franchise_count': franchise_count,
        'institute_count': institute_count,
        'user_count': student_count + trainer_count + franchise_count + institute_count
    }

    return render(request, 'user_student.html', context)




def user_trainer(request):
    institute_count = InstituteProfile.objects.all().count()

    all_trainer = TrainerProfile.objects.all()

    '''franchise_count'''
    franchise_count = FranchiseProfile.objects.all().count()



    '''student'''

    student_count = Student.objects.all().count()

    '''trainer'''

    trainer_count = TrainerProfile.objects.all().count()

    context = {

        'all_trainer': all_trainer,
        'trainer_count': trainer_count,
        'student_count': student_count,
        'franchise_count': franchise_count,
        'institute_count': institute_count,
        'user_count': student_count + trainer_count + franchise_count + institute_count
    }

    return render(request,'user_trainer.html',context)








def trainerProfile(request , username):
    user = User.objects.get(username = username)
    trainer = TrainerProfile.objects.get(user = user)
    profile = 'trainer'
    context = {'trainer':trainer,'profile':profile}
    return render(request,'user_profile.html',context)

def instituteProfile(request , username):
    user = User.objects.get(username = username)
    institute = InstituteProfile.objects.get(user = user)
    profile = 'institute'
    context = {'institute':institute,'profile':profile}
    return render(request,'user_profile.html',context)

def franchiseProfile(request , username):
    user = User.objects.get( username = username )
    franchise = FranchiseProfile.objects.get(user = user)
    profile = 'franchise'
    context = {'franchise':franchise,'profile':profile}
    return render(request,'user_profile.html',context)

def studentProfile(request , username):
    user = User.objects.get(username = username)
    student = Student.objects.get(user = user)
    profile = 'student'
    context = {'student':student,'profile':profile }
    return render(request,'user_profile.html',context)



def coursedetailView(request,slugfield):
    course = CourseDetails.objects.get(slug = slugfield)
    context = {'course':course}
    return render(request,'multiuser_totalcourse.html',context)



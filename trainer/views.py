from django.shortcuts import render, redirect
from.form import CourseDetailsForm, VideoForm, CategoriesForm
from inventory.models import CourseVideos, CourseDetails
from django.contrib import messages
from multiuser.models import  TrainerProfile
# Create your views here.

def trainerProfile(request):
    return render(request,'trainer/trainer-profile-look.html')

def addCourse(request):
    return render(request,'trainer/T-addcourses.html')

def students(request):
    return render(request,'trainer/T-student.html')

def trainerCourses(request):
    return render(request,'trainer/T-coursesdetails.html')



def addCourse1(request):

    ''' add course from user '''

    form = CourseDetailsForm()
    form1 = VideoForm()
    template = 'offline.html'
    context = {'form':form,'form1':form1}
    if request.method == "POST":
        form1 = VideoForm(request.POST, request.FILES)
        form = CourseDetailsForm(request.POST, request.FILES)
        email=request.user.email
        trainer1=TrainerProfile.objects.get(trainerEmail=email)
        if form1.is_valid() or form.is_valid():
            courseObj = form.save()
            name=courseObj.courseName
            videoObj=form1.save()
            pk = videoObj.id
            CourseDetails.objects.filter(courseName=name).update(trainer=trainer1)
            CourseVideos.objects.filter(id=pk).update(course=courseObj)
            messages.info(request,'Course is added succesfully')
            return redirect ('trainer_profile')
        else:
            messages.info(request,'Error are {} {}'.format(form.errors , form1.errors))
            return  render(request, template,context)
    return render(request, template,context)



def addCategory(request):
    form = CategoriesForm()
    context = {'form':form}
    if request.method == 'POST':
        form = CategoriesForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request,'New category is added successfully')
            return redirect('add_course')
        else:
            messages.info(request,form.errors)
        return render(request, 'add-category.html',context)

    return render(request,'add-category.html',context)



def onlineaddcourse(request):

    ''' add course from user '''

    form = CourseDetailsForm()
    form1 = VideoForm()
    template = 'Addcourse.html'
    context = {'form':form,'form1':form1}
    if request.method == "POST":
        email=request.user.email
        traine1=TrainerProfile.objects.get(trainerEmail=email)
        form1 = VideoForm(request.POST, request.FILES)
        form = CourseDetailsForm(request.POST, request.FILES)
        if form1.is_valid() or form.is_valid():
            courseObj = form.save()
            videoObj=form1.save()
            pk = videoObj.id
            name=courseObj.courseName
            CourseVideos.objects.filter(id=pk).update(course=courseObj)
            CourseDetails.objects.filter(courseName=name).update(trainer=traine1)
            messages.info(request,'Course is added succesfully')
            return redirect ('trainer_profile')
        else:
            messages.info(request,'Error are {} {}'.format(form.errors , form1.errors))
            return render(request, template,context)
    return render(request, template,context)
from django.shortcuts import render , redirect
from django.http import HttpResponse
from .models import *
from .forms import CourseDetailsForm , CategoriesForm , VideoForm
from django.contrib import messages
from django.shortcuts import get_object_or_404



def inventory(request):

    ''' show courses in tabel format '''

    courseDetails = CourseDetails.objects.all()
    context = {'courseDetails':courseDetails}
    return render(request,'view_courses.html',context)

def addCourse(request):

    ''' add course from user '''

    form = CourseDetailsForm()
    form1 = VideoForm()
    template = 'add_course.html'

    context = {'form':form,'form1':form1}
    if request.method == "POST":
        form1 = VideoForm(request.POST, request.FILES)
        form = CourseDetailsForm(request.POST, request.FILES)
        if form1.is_valid() or form.is_valid():
            courseObj = form.save()
            videoObj=form1.save()
            pk = videoObj.id
            CourseVideos.objects.filter(id=pk).update(course = courseObj)
            messages.info(request,'Course is added succesfully')
            redirect ('inventory')
        else:
            messages.info(request,'Error are {} {}'.format(form.errors , form1.errors))
            redirect ('inventory')
    return render(request, template,context)


def editCourse(request , slugfield):

    ''' edit details of already added course 
        slugfield is unique to every course '''

    courseDetails = get_object_or_404( CourseDetails ,slug = slugfield)
    form = CourseDetailsForm(instance = courseDetails)
    courseVideos = CourseVideos.objects.get(course = courseDetails)
    form1 = VideoForm( instance =courseVideos )
    if request.method == 'POST':
        form1 = VideoForm(request.POST, request.FILES ,instance = courseVideos )
        form = CourseDetailsForm(request.POST, request.FILES,instance =courseDetails )
        if form.is_valid() or form1.is_valid():
            form.save()
            form1.save()
            messages.info(request,'Changes are made successfully')
        else:
            messages.info(request,form.errors)
        return redirect('inventory')

    context = {'form':form,'form1':form1,'courseDetails':courseDetails}
    return render(request,'edit_course.html',context)

 


def deleteCourse(request , pk):

    ''' delete course of id = pk '''

    course = get_object_or_404(CourseDetails ,id=pk)
    courseVideos = CourseVideos.objects.get(course = course)
    if request.method == 'POST':
        course.delete()
        courseVideos.delete()
        messages.info(request,'Course is deleted successfully')
        return redirect('inventory')
    return render(request,'view_courses.html')
    


def Course(request):
    '''courses'''
    courseDetails = CourseDetails.objects.all()

    '''count'''
    course_count=CourseDetails.objects.all().count()

    all_course = CourseDetails.objects.all()
    '''filter'''

    ""'CAtegory_Course'""
    Course_Category=Categories.objects.count()

    '''courseStatus_wise'''
    a,i=0,0
    for a_ctive in all_course:
        if a_ctive.courseStatus=='active':
            a+=1
        else:
            i+=1


    thank=True
    context={
        'category_course_count':Course_Category,
        'course_count':course_count,
        'active_course_count':a,
        'inactive_course_count':i,
        'courseDetails': courseDetails,
        'thank':thank

         }
    return render(request,'course.html',context)



def showCategory(request):

    ''' show category in tabel format '''

    categories = Categories.objects.all()
    context = {'categories':categories}
    return render(request,'view_category.html',context)


def addCategory(request):
    form = CategoriesForm()
    if request.method == 'POST':
        form = CategoriesForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request,'New category is added successfully')
        else:
            messages.info(request,form.errors)
        return redirect('show_category')
    context = {'form':form}
    return render(request,'add-category.html',context)


def editCategory(request , slugfield):

    categories = get_object_or_404(Categories ,slug = slugfield)
    form = CategoriesForm(instance = categories)
    if request.method == 'POST':
        form = CategoriesForm(request.POST,instance =categories )
        if form.is_valid():
            form.save()
            messages.info(request,'Changes are made successfully')
        else:
            messages.info(request,form.errors)
        return redirect('show_category')

    context = {'form':form,'categories':categories}
    return render(request,'edit_categories.html',context)



def deleteCategory(request , pk):

    ''' delete course of id = pk '''

    category = get_object_or_404(Categories ,id=pk)
    if request.method == 'POST' or 'GET':
        category.delete()
        messages.info(request,'Category is deleted successfully')
        return redirect('show_category')
    return render(request,'view_category.html')


def detailView(request,slugfield):
    course = CourseDetails.objects.get(slug = slugfield)
    context = {'course':course}
    return render(request,'course_detail_view.html',context)





















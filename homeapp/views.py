from django.shortcuts import render
from inventory.models import *
from django.shortcuts import get_object_or_404
# Create your views here.

def homepage1(request):
    courseDetails = CourseDetails.objects.all()
    messages=True
    return render(request,'index_main.html',{'courseDetails':courseDetails, "messages":messages , "name":request.user.username })


def homePage(request):
    courseDetails = CourseDetails.objects.all()
    return render(request,'index_main.html',{'courseDetails':courseDetails })


def coursePage(request , slugfield ):
    course = get_object_or_404(CourseDetails , slug = slugfield)
    context = {'course':course}
    return render(request,'homepage_course_details.html',context)

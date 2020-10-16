from django.db import models
from inventory.models import CourseDetails
from multiuser.models import User
from phone_field import PhoneField
from mptt.models import MPTTModel, TreeForeignKey
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import AbstractUser

gender=(('Male','Male'),('Female','Female'),('others','Transgender'))


class Student(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='student')
    student_FullName = models.CharField(max_length=150, blank=True)
    student_About=models.CharField(blank=True,null=False,max_length=2500)
    student_gender = models.CharField(choices=gender,max_length=50)

    student_Image = models.FileField(upload_to='Student_image/', null=True , blank=True)
    stdent_Email = models.EmailField(max_length=111)
    student_created_at = models.DateTimeField(auto_now_add=True)

    course_id = models.ManyToManyField(CourseDetails, default=1)
    student_PhoneNo1 = PhoneNumberField(null=False, blank=False, unique=False)
    student_PhoneNo2 = PhoneNumberField(null=False, blank=False, unique=False)
    student_Address=models.CharField(max_length=250,default='')
    student_City = models.CharField(max_length=100, default='')
    student_Zipcode= models.IntegerField(default=273003)
    student_State = models.CharField(max_length=100, default='')
    student_Country = models.CharField(max_length=100, default='')
    objects = models.Manager()

    def __str__(self):
        return self.student_FullName



    @property
    def getImageURL(self):
        try:
            url = self.Student_Image.url
        except:
            url = ''
        return url

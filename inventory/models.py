from django.db import models
from multiuser.models import *
from mptt.models import MPTTModel, TreeForeignKey
import datetime
from django.utils import timezone
from multiselectfield import MultiSelectField
from django.db.models.signals import pre_save



  

class Categories(MPTTModel):

    statusChoice = (
        ('Active', 'Active'),
        ('Inactive', 'Inactive'),
        ('Available', 'Available')
        )
  
    name = models.CharField(max_length = 250 , unique =True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    seo_title = models.CharField(max_length=70)
    seo_description =models.CharField(max_length=160)
    slug = models.SlugField(max_length=255 , unique =True)
    categoryStatus = models.CharField(max_length = 30 , choices = statusChoice, null=True , blank=True)
    categoryCreated = models.DateTimeField(auto_now_add=True)
    seo_keywords = models.CharField(max_length=160)
    class MPTTMeta:
        order_insertion_by = ['name']
   
    def __str__(self):
        return self.name


class CourseDetails(models.Model):
    
    statusChoice = (
        ('Active', 'Active'),
        ('Inactive', 'Inactive'),
        ('Available', 'Available')
        )

    belongChoice = (
        ('Trainer','Trainer'),
        ('Intitute','Institute'),
        ('Franchise','Franchise'),
        )

    weekdayChoice = (
        ('Monday','Monday'),
        ('Tuesday','Tuesday'),
        ('Wednesday','Wednesday'),
        ('Thursday','Thursday'),
        ('Friday','Friday'),
        ('Saturday','Saturday'),
        ('Sunday','Sunday')
        )
    
    trainer = models.ForeignKey(TrainerProfile , on_delete=models.SET_NULL ,  blank = True , null = True)
    institute = models.ForeignKey(InstituteProfile, on_delete=models.SET_NULL ,  blank = True , null = True)
    franchise = models.ForeignKey(FranchiseProfile, on_delete=models.SET_NULL ,  blank = True , null = True)
    courseName = models.CharField(max_length = 400 , null = True , blank=True)
    courseDescription = models.TextField(null = True , blank =True)
    courseCategory = models.ForeignKey(Categories , on_delete=models.CASCADE ,  blank = True , null = True)
    courseOnline =  models.BooleanField(blank = True , null =True , default = False)
    courseImage = models.FileField(upload_to='images/', null=True , blank=True)
    courseLive =  models.BooleanField(blank = True , null =True,default = False)
    courseOffline =  models.BooleanField(blank = True , null =True,default = False)
    courseStatus = models.CharField(max_length = 30 , choices = statusChoice, null=True , blank=True)
    coursePrice =  models.DecimalField(max_digits=10,decimal_places=2 , null=True , blank=True)
    promocode =models.CharField(max_length=160 , null=True ,  blank=True)
    priceDiscount = models.DecimalField(max_digits=10,decimal_places=2,null=True , blank=True)
    totalPriceDiscount = models.DecimalField(max_digits=10,decimal_places=2,null=True , blank=True)
    courseCity = models.CharField(max_length = 200 , null = True , blank=True)
    courseState =  models.CharField(max_length = 200 , null = True , blank=True)
    courseCountry = models.CharField(max_length = 200 , null = True,blank=True)
    offlineAddress = models.TextField(null=True , blank = True)
    offlineClassStrength = models.IntegerField(null=True ,  blank=True)
    offlineTiming = models.DateTimeField(auto_now_add=False,null=True ,  blank=True)
    offlineWeekday = MultiSelectField(choices=weekdayChoice,null=True ,  blank=True)
    onlineWeekday = MultiSelectField(choices=weekdayChoice,null=True ,  blank=True)
    onlineTiming = models.DateTimeField(auto_now_add=False,null=True ,  blank=True)
    courseBelong = models.CharField(max_length = 30 , choices = belongChoice, null=True , blank=True)
    seo_title = models.CharField(max_length=70)
    seo_description =models.CharField(max_length=160)
    seo_keywords =models.CharField(max_length=160)
    slug = models.SlugField(max_length=255 , unique =True)
    introVideo= models.FileField(upload_to='IntroVideos/', null=True,blank=True)
    courseCreated = models.DateTimeField(auto_now_add=True)
    
    
    class Meta:
        ordering = ['-courseCreated'] 

    def __str__(self):
        return self.courseName


    def convert_to_ruppes(self,_id):
        return self.coursePrice * 70

    def get_total_price(self,_id):
        total = self.coursePrice
        if self.priceDiscount == 0:
            return total
        else:
            total = self.coursePrice - (self.coursePrice * (self.priceDiscount/100) )
            return total

    @property
    def getImageURL(self):
        try:
            url = self.courseImage.url
        except:
            url = ''
        return url

    @property
    def getIntoVideoURL(self):
        try:
            url = self.introVideo.url
        except:
            url = ''
        return url


    
            
            

    

class CourseVideos(models.Model):
    course = models.ForeignKey(CourseDetails , on_delete=models.SET_NULL ,  blank = True , null = True)
    courseVideoName= models.CharField(max_length=500,null=True , blank = True)
    courseVideoFile= models.FileField(upload_to='videos/', null=True,blank=True)
    courseVideoDescription= models.TextField(null=True , blank = True)
    courseVideoCreated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)

    @property
    def videoURL(self):
        try:
            url = self.courseVideoFile.url
        except:
            url = ''
        return url






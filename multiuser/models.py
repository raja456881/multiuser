from django.contrib.auth.models import AbstractBaseUser,BaseUserManager, PermissionsMixin,AbstractUser
from django.db import models
from django.utils import timezone
from django.db import models
from phone_field import PhoneField
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth import get_user_model


approvalChoice = (
        ('Verified', 'Verified'),
        ('Pending', 'Pending'),
        ('Discarded', 'Discarded'),
        )

genderChoice = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    )

class User(AbstractUser):

    is_trainer = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_student=models.BooleanField(default=False)
    is_institute = models.BooleanField(default=False)
    is_franchise = models.BooleanField(default=False)


class AdminProfile(models.Model):

    user = models.OneToOneField(User , on_delete=models.CASCADE,primary_key=True,related_name='admin')
    adminFullName = models.CharField(max_length=150 , blank=True)
    adminGender = models.CharField(max_length = 30 , choices =genderChoice , default="")
    adminAbout= models.TextField(blank=True , null=True)
    adminEmail = models.EmailField(max_length = 100 , blank = True)
    adminImage = models.FileField(upload_to='Admin_image/', null=True , blank=True)
    adminPhoneNo1 = PhoneNumberField(null=False, blank=False, unique=False)
    adminPhoneNo2 = PhoneNumberField(null=False, blank=False, unique=False)
    adminAddress = models.CharField(max_length= 500 , blank = True)
    adminCity = models.CharField(blank=True,max_length=50)
    adminPostalCode = models.IntegerField(blank=True,null=True)
    adminState = models.CharField(blank=True,max_length=50)
    adminCountry = models.CharField(max_length=20,blank=False,default='')
    adminStatus = models.CharField(max_length = 30 , choices = approvalChoice, default="Pending")
    adminAddedDate = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.adminFullName

    @property
    def getImageURL(self):
        try:
            url = self.adminImage.url
        except:
            url = ''
        return url

class TrainerProfile(models.Model):
    user = models.OneToOneField(User , on_delete=models.CASCADE,primary_key=True)
    trainerFullName = models.CharField(max_length=150 , blank=True)
    trainerGender = models.CharField(max_length = 30 , choices =genderChoice , default="")
    trainerAbout= models.TextField(blank=True , null=True)
    trainerEmail = models.EmailField(max_length = 100 , blank = True)
    trainerImage = models.FileField(upload_to='Trainer_image/', null=True , blank=True)
    trainerPhoneNo1 = PhoneNumberField(null=False, blank=False, unique=False)
    trainerPhoneNo2 = PhoneNumberField(null=False, blank=False, unique=False)
    trainerAddress = models.CharField(max_length= 500 , blank = True)
    trainerCity = models.CharField(blank=True,max_length=50)
    trainerPostalCode = models.IntegerField(blank=True,null=True)
    trainerState = models.CharField(blank=True,max_length=50)
    trainerCountry = models.CharField(max_length=20,blank=False,default='')
    trainerStatus = models.CharField(max_length = 30 , choices = approvalChoice, default="Pending")
    trainerAddedDate = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.trainerFullName

    @property
    def getImageURL(self):
        try:
            url = self.trainerImage.url
        except:
            url = ''
        return url

class InstituteProfile(models.Model):

    user = models.OneToOneField(User , on_delete=models.CASCADE,primary_key=True)
    instituteName = models.CharField(max_length = 200 , blank = True)
    instituteAbout= models.TextField(blank=True , null=True)
    instituteEmail = models.EmailField(max_length = 100 , blank = True)
    instituteImage = models.FileField(upload_to='Institute_image/', null=True , blank=True)
    institutePhoneNo1 = PhoneNumberField(null=True, blank=True, unique=False)
    institutePhoneNo2 = PhoneNumberField(null=True, blank=True, unique=False)
    instituteAddress = models.CharField(max_length= 500 , blank = True)
    instituteCity = models.CharField(blank=True,max_length=50)
    institutePostalCode = models.IntegerField(blank=True,null=True)
    instituteState = models.CharField(blank=True,max_length=50)
    instituteCountry = models.CharField(max_length=20,blank=False,default='')
    instituteStatus = models.CharField(max_length = 30 , choices = approvalChoice,default="Pending")
    instituteAddedDate = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.instituteName

    @property
    def getImageURL(self):
        try:
            url = self.instituteImage.url
        except:
            url = ''
        return url

class FranchiseProfile(models.Model):

    user = models.OneToOneField(User , on_delete=models.CASCADE,primary_key=True)
    franchiseName = models.CharField(max_length = 200 , blank = True)
    franchiseAbout= models.TextField(blank=True , null=True)
    franchiseEmail = models.EmailField(max_length =100 , blank = True)
    franchiseImage = models.FileField(upload_to='Franchise_image/', null=True , blank=True)
    franchisePhoneNo1 = PhoneNumberField(null=True, blank=True, unique=False)
    franchisePhoneNo2 = PhoneNumberField(null=True, blank=True, unique=False)
    franchiseAddress = models.CharField(max_length= 500 , blank = True)
    franchiseCity = models.CharField(blank=True,max_length=50)
    franchisePostalCode =models.IntegerField(blank=True,null=True)
    franchiseState = models.CharField(blank=True,max_length=50)
    franchiseCountry = models.CharField(max_length=20,blank=False,default='')
    franchiseStatus = models.CharField(max_length = 30 , choices = approvalChoice, default="Pending")
    franchiseAddedDate = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.franchiseName

    @property
    def getImageURL(self):
        try:
            url = self.franchiseImage.url
        except:
            url = ''
        return url



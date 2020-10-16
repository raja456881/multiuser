from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import  UserCreationForm
from .models import User,AdminProfile,TrainerProfile,InstituteProfile,FranchiseProfile
from student.models import Student
from django.db import transaction

class AdminSignUpForm(UserCreationForm):
    email = forms.CharField(required=True)
    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self,commit=True):
        user = super().save(commit=False)
        user.is_admin = True
        user.save()
        if commit:
            admin=AdminProfile.objects.create(user=user)
            admin.adminFullName=self.cleaned_data.get("username")
            admin.adminEmail = self.cleaned_data.get("email")
            admin.save()


        return user


class FranchiseSignUpForm(UserCreationForm):

    email = forms.CharField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self,commit=True):
        user = super().save(commit=False)
        user.is_franchise = True
        user.save()
        if commit:
            admin=FranchiseProfile.objects.create(user=user)
            admin.franchiseName=self.cleaned_data.get("username")
            admin.franchiseEmail = self.cleaned_data.get("email")
            admin.save()


        return user



class InstituteSignUpForm(UserCreationForm):
    email = forms.CharField(required=True)
    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self,commit=True):
        user = super().save(commit=False)
        user.is_institute = True
        user.save()
        if commit:
            institute=InstituteProfile.objects.create(user=user)
            institute.instituteName=self.cleaned_data.get("username")
            institute.instituteEmail = self.cleaned_data.get("email")
            institute.save()


        return user



class TrainerSignUpForm(UserCreationForm):
    email = forms.CharField(required=True)
    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self,commit=True):
        user = super().save(commit=False)
        user.is_trainer = True
        user.save()
        if commit:
            trainer=TrainerProfile.objects.create(user=user)
            trainer.trainerFullName=self.cleaned_data.get("username")
            trainer.trainerEmail = self.cleaned_data.get("email")
            trainer.save()


        return user




class StudentSignUpForm(UserCreationForm):
    email = forms.CharField(required=True)
    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self,commit=True):
        user = super().save(commit=False)
        user.is_student = True
        user.save()
        if commit:
            student=Student.objects.create(user=user)
            student.student_FullName=self.cleaned_data.get("username")
            student.stdent_Email = self.cleaned_data.get("email")
            student.save()


        return user



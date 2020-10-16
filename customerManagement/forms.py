from django.forms import ModelForm
from django import forms
from student.models import Student
from multiuser.models import AdminProfile , TrainerProfile , InstituteProfile , FranchiseProfile,User
from django.contrib.auth.forms import UserCreationForm

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','username','password']
        exclude = ['user', 'time']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control','required': True}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
            'username': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
            'password': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
            }

class AdminForm(forms.ModelForm):
    class Meta:
        model = AdminProfile
        fields = '__all__'
        exclude = ['user', 'time']

        widgets = {
            'adminFullName': forms.TextInput(attrs={'class':'form-control','required': True}),
            'adminEmail': forms.TextInput(attrs={'class':'form-control', 'required': True}),
            'adminAbout': forms.Textarea(attrs={'class':'form-control','rows':2}),
            'adminGender': forms.Select(attrs={'class':'custom-select', 'required': True}),
            'adminPhoneNo1': forms.TextInput(attrs={'class':'form-control', 'required': True}),
            'adminPhoneNo2': forms.TextInput(attrs={'class':'form-control'}),
            'adminAddress': forms.TextInput(attrs={'class':'form-control','required': True}),
            'adminState': forms.TextInput(attrs={'class':'form-control','required': True}),
            'adminCity': forms.TextInput(attrs={'class':'form-control','required': True}),
            'adminPostalCode': forms.NumberInput(attrs={'class':'form-control','required': True}),
            'adminCountry': forms.TextInput(attrs={'class':'form-control', 'required': True}),
            'adminStatus': forms.Select(attrs={'class':'custom-select', 'required': True}),
              }

class TrainerForm(forms.ModelForm):
    class Meta:
        model = TrainerProfile
        fields = '__all__'
        exclude = ['user', 'time']

        widgets = {
            'trainerFullName': forms.TextInput(attrs={'class': 'form-control','required': True}),
            'trainerEmail': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
            'trainerAbout': forms.Textarea(attrs={'class':'form-control','rows':2}),
            'trainerGender': forms.Select(attrs={'class':'custom-select', 'required': True}),
            'trainerPhoneNo1': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
            'trainerPhoneNo2': forms.TextInput(attrs={'class': 'form-control'}),
            'trainerAddress': forms.TextInput(attrs={'class': 'form-control','required': True}),
            'trainerCity': forms.TextInput(attrs={'class':'form-control','required': True}),
            'trainerPostalCode': forms.NumberInput(attrs={'class':'form-control','required': True}),
            'trainerState': forms.TextInput(attrs={'class': 'form-control','required': True}),
            'trainerCountry': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
            'trainerStatus': forms.Select(attrs={'class': 'custom-select', 'required': True}),
              }

class InstituteForm(forms.ModelForm):
    class Meta:
        model = InstituteProfile  
        fields = '__all__'
        exclude = ['user', 'time']

        widgets = {
            'instituteName': forms.TextInput(attrs={'class': 'form-control','required': True}),
            'instituteEmail': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
            'instituteAbout': forms.Textarea(attrs={'class':'form-control','rows':2}),
            'institutePhoneNo1': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
            'institutePhoneNo2': forms.TextInput(attrs={'class': 'form-control'}),
            'instituteAddress': forms.TextInput(attrs={'class': 'form-control','required': True}),
            'instituteState': forms.TextInput(attrs={'class': 'form-control','required': True}),
            'instituteCity': forms.TextInput(attrs={'class':'form-control','required': True}),
            'institutePostalCode': forms.NumberInput(attrs={'class':'form-control','required': True}),
            'instituteCountry': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
            'instituteStatus': forms.Select(attrs={'class': 'custom-select', 'required': True}),
              }

class FranchiseForm(forms.ModelForm):
    class Meta:
        model = FranchiseProfile   
        fields = '__all__'
        exclude = ['user', 'time']

        widgets = {
            'franchiseName': forms.TextInput(attrs={'class': 'form-control','required': True}),
            'franchiseEmail': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
            'franchiseAbout': forms.Textarea(attrs={'class':'form-control','rows':2}),
            'franchisePhoneNo1': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
            'franchisePhoneNo2': forms.TextInput(attrs={'class': 'form-control'}),
            'franchiseAddress': forms.TextInput(attrs={'class': 'form-control','required': True}),
            'franchiseState': forms.TextInput(attrs={'class': 'form-control','required': True}),
            'franchiseCity': forms.TextInput(attrs={'class':'form-control','required': True}),
            'franchisePostalCode': forms.NumberInput(attrs={'class':'form-control','required': True}),
            'franchiseCountry': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
            'franchiseStatus': forms.Select(attrs={'class': 'custom-select', 'required': True}),
              }



class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
        exclude = ['user', 'time']

        widgets = {
            'student_name': forms.TextInput(attrs={'class': 'form-control','required': True}),
            'stdent_Email': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
            'student_About': forms.Textarea(attrs={'class':'form-control','rows':2}),
            'student_gender': forms.Select(attrs={'class':'custom-select', 'required': True}),
            'student_PhoneNo1': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
            'student_PhoneNo2': forms.TextInput(attrs={'class': 'form-control'}),
            'student_Address': forms.TextInput(attrs={'class': 'form-control','required': True}),
            'student_City': forms.TextInput(attrs={'class':'form-control','required': True}),
            'student_Zipcode': forms.NumberInput(attrs={'class':'form-control','required': True}),
            'student_State': forms.TextInput(attrs={'class': 'form-control','required': True}),
            'student_Country': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
            'trainerStatus': forms.Select(attrs={'class': 'custom-select', 'required': True}),
              }
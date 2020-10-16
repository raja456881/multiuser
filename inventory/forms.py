from django.forms import ModelForm
from django import forms
from .models import CourseDetails , Categories , CourseVideos



class CourseDetailsForm(forms.ModelForm):
    weekdayChoice = (
        ('Monday','Monday'),
        ('Tuesday','Tuesday'),
        ('Wednesday','Wednesday'),
        ('Thursday','Thursday'),
        ('Friday','Friday'),
        ('Saturday','Saturday'),
        ('Sunday','Sunday')
        )

    class Meta:
        model = CourseDetails
        fields = ['courseName','courseCategory','courseDescription','courseOnline','courseLive','courseOffline','seo_keywords',
                  'courseStatus','coursePrice','courseCity','courseState','courseCountry','priceDiscount','courseImage',
                  'courseBelong','seo_title','seo_description','slug' ,'trainer','institute','franchise','totalPriceDiscount','introVideo',
                  'offlineTiming','onlineTiming','offlineAddress','offlineClassStrength','offlineWeekday','onlineWeekday','promocode']
       

        widgets ={
            'courseName':forms.TextInput(attrs={'class':'form-control','placeholder':'eg:-React','required':True}),
            'courseDescription':forms.Textarea(attrs={'class':'form-control','placeholder':'Full Python Course','rows':3,'required':True}),
            'courseCategory':forms.Select(attrs={'class':'custom-select','required':True}),
            'courseStatus':forms.Select(attrs={'class':'custom-select','required':True}),
            'courseCity':forms.TextInput(attrs={'class':'form-control','placeholder':'eg:-Mumbai'}),
            'courseState':forms.TextInput(attrs={'class':'form-control','placeholder':'eg:-Maharashtra'}),
            'courseCountry':forms.TextInput(attrs={'class':'form-control','placeholder':'eg:-India'}),
            'coursePrice':forms.NumberInput(attrs={'class':'form-control','placeholder':'$100','required':True}),
            'priceDiscount':forms.NumberInput(attrs={'class':'form-control','placeholder':'10',}),
            'courseOnline':forms.NullBooleanSelect(attrs={'class':'custom-select','required':True}),
            'courseLive':forms.NullBooleanSelect(attrs={'class':'custom-select','required':True}),
            'courseOffline':forms.NullBooleanSelect(attrs={'class':'custom-select','required':True}),
            'seo_title':forms.TextInput(attrs={'class':'form-control','required':True}),
            'seo_description':forms.TextInput(attrs={'class':'form-control','required':True}),
            'seo_keywords':forms.TextInput(attrs={'class':'form-control','required':True}),
            'slug':forms.TextInput(attrs={'class':'form-control','required':True}),
            'trainer':forms.Select(attrs={'class':'form-control'}),
            'institute':forms.Select(attrs={'class':'form-control'}),
            'franchise':forms.Select(attrs={'class':'form-control'}),
            'offlineTiming':forms.DateTimeInput(attrs={'class':'form-control','placeholder':'2020-09-15 14:30'}),
            'onlineTiming':forms.DateTimeInput(attrs={'class':'form-control','placeholder':'2020-09-15 14:30'}),
            'offlineAddress':forms.Textarea(attrs={'class':'form-control','rows':2}),
            'offlineClassStrength':forms.NumberInput(attrs={'class':'form-control'}),
            #'offlineWeekday':forms.CheckboxSelectMultiple(attrs={'class':''}),
            #'onlineWeekday':forms.CheckboxSelectMultiple(),
            'promocode':forms.TextInput(attrs={'class':'form-control','placeholder':'eg:-Offer20'}),
            'totalPriceDiscount':forms.NumberInput(attrs={'class':'form-control'})
        }


class CategoriesForm(forms.ModelForm):
    class Meta:
        model = Categories
        fields = ['parent','name','seo_title','seo_description','categoryStatus','slug','seo_keywords']

        widgets = {
                'parent':forms.Select(attrs={'class':'form-control'}),
                'name':forms.TextInput(attrs={'class':'form-control','placeholder':'Web development','required':True}),
                'categoryStatus':forms.Select(attrs={'class':'custom-select','required':True}),
                'seo_title':forms.TextInput(attrs={'class':'form-control','required':True}),
                'seo_description':forms.TextInput(attrs={'class':'form-control','required':True}),
                'seo_keywords':forms.TextInput(attrs={'class':'form-control','required':True}),
                'slug':forms.TextInput(attrs={'class':'form-control','required':True}),
            }


class TotalCourseForm(forms.ModelForm):
    class Meta:
        model = CourseDetails
        fields = ['courseName', 'courseCategory', 'courseStatus', 'courseState', 'courseCountry', 'courseBelong']

        widgets = {
            'courseName': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'eg:-React', 'required': True}),
            'courseBelong': forms.Select(attrs={'class': 'custom-select', 'required': True}),
            'courseCategory': forms.Select(attrs={'class': 'custom-select', 'required': True}),
            'courseStatus': forms.Select(attrs={'class': 'custom-select', 'required': True}),
            'courseState': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'eg:-Maharashtra', 'required': True}),
            'courseCountry': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'eg:-India', 'required': True}),
              }

class VideoForm(forms.ModelForm):
    class Meta:
        model = CourseVideos
        fields = ['courseVideoName','courseVideoFile','courseVideoDescription']

        widgets = {
            'courseVideoName': forms.TextInput(attrs={'class': 'form-control'}),
            'courseVideoDescription': forms.Textarea(attrs={'class': 'form-control','rows':2}),
              }

        

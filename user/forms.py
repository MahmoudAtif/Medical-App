from cProfile import label
from dataclasses import fields
from pyexpat import model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import * 
from accounts.models import * 

class UserForm(UserCreationForm):
    username=forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'اسم المستخدم'
    }))

    email=forms.CharField(widget=forms.EmailInput(attrs={
        'class':'form-control',
        'placeholder':'البريد الاكتروني'
    }))

    password1=forms.CharField(widget=forms.PasswordInput(attrs={
        'class':'form-control',
        'placeholder':'الرقم السري'
    }))

    password2=forms.CharField(widget=forms.PasswordInput(attrs={
        'class':'form-control',
        'placeholder':'تاكيد الرقم السري'

    }))
    class Meta:
        model=User
        fields=['username','email','password1','password2']




class ProfileForm(forms.ModelForm):
    class Meta:
        model=Doctor
        fields=['name','Specialist_doctor','address' , 'Waiting_time'  , 'working_hours' , 'phone_number', 'who_i', 'gender', 'price', 'facebook' ,'twitter' ,'gmail' ,'image']
        widgets={
            'name':forms.TextInput(attrs={
                'class':'form-control'
            }),
            'Specialist_doctor':forms.Select(attrs={
                'class':'form-control',

            }),
            'address':forms.TextInput(attrs={
                'class':'form-control'
            }),
            'Waiting_time':forms.NumberInput(attrs={
                'class':'form-control'
            }),
            'working_hours':forms.NumberInput(attrs={
                'class':'form-control'
            }),
            'phone_number':forms.NumberInput(attrs={
                'class':'form-control'
            }),
            'who_i':forms.Textarea(attrs={
                'class':'form-control'
            }),
            'gender':forms.Select(attrs={
                'class':'form-control'
            }),
            'price':forms.NumberInput(attrs={
                'class':'form-control'
            }),
            'facebook':forms.TextInput(attrs={
                'class':'form-control'
            }),
            'twitter':forms.TextInput(attrs={
                'class':'form-control'
            }),
            'gmail':forms.TextInput(attrs={
                'class':'form-control'
            }),
            'image':forms.FileInput(attrs={
                'class':'form-control'
            })
        }



class ServiceForm(forms.ModelForm):
    class Meta:
        model=DoctorServices
        fields=['service']
        widgets={
            'service':forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'اضافة خدمه',
            })
        }



class ImageForm(forms.ModelForm):
    class Meta:
        model=ClinicImages
        fields=['image']
        widgets={
            'service':forms.FileInput(attrs={
                'class':'form-control',
                'placeholder':'اضافة صوره',
            })
        }
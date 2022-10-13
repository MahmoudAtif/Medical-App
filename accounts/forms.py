from dataclasses import fields
from pyexpat import model
from tkinter import Widget
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import * 



class AppointmentForm(forms.ModelForm):
    class Meta:
        model=Appointment
        fields=['details' , 'time']
        widgets={
            'details':forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'سببب الكشف'
            }),
             'time':forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'ميعاد الشكف '
            })
        }


class CommnetForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields=['comment']


class RateForm(forms.ModelForm):
    class Meta:
        model=Rate
        fields=['rate']
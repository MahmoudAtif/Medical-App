import django_filters

from user.models import Doctor
from django import forms





class FilterForm(django_filters.FilterSet):
    name=forms.CharField(widget=forms.TextInput(attrs={
        'placeholder':'إسم الدكتور',
    }))

    address=forms.CharField(widget=forms.TextInput(attrs={
        'placeholder':'العنوان'
    }))
    
    Specialist_doctor=forms.CharField(widget=forms.Select(attrs={
        'placeholder':'التخصص'
    }))

    class Meta:
        model=Doctor
        fields=['name','address','Specialist_doctor']
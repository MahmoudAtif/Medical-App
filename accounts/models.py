from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from math import *
from user import models as usermodels 
# Create your models here.


class Appointment(models.Model):
    doctor=models.ForeignKey(User ,verbose_name=' اسم الدكتور ', on_delete=models.CASCADE , related_name='doctor_appointment')
    patient=models.ForeignKey(User ,verbose_name=' اسم المريض ', on_delete=models.CASCADE , related_name='patient_appointment')
    details=models.CharField(verbose_name=' اسباب الكشف' , max_length=50 , null=True , blank=True)
    time=models.CharField(verbose_name='ميعاد الشكف ' , max_length=50 , null=True , blank=True)
    date_created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.doctor)
    

class ClinicImages(models.Model):   
    clinic=models.ForeignKey(usermodels.Doctor, verbose_name=("عياده الدكتور"), on_delete=models.CASCADE, related_name='clinicImages')
    image=models.ImageField(upload_to='clinicImages')

    def __str__(self):
        return str(self.clinic)
    
class DoctorServices(models.Model):   
    clinic=models.ForeignKey(usermodels.Doctor, verbose_name=("عياده الدكتور"), on_delete=models.CASCADE, related_name='doctorServices')
    service=models.CharField(verbose_name=('الخدمه'), max_length=50)

    def __str__(self):
        return str(self.clinic.user)



class Comment(models.Model):
    doctor=models.ForeignKey(User ,verbose_name=' اسم الدكتور ', on_delete=models.CASCADE , related_name='doctorComment')
    patient=models.ForeignKey(User ,verbose_name=' اسم المريض ', on_delete=models.CASCADE , related_name='patientComment')
    comment=models.CharField(verbose_name=("التعليق"), max_length=50)
    date_created=models.DateTimeField(verbose_name=("تاريخ التعليق"), auto_now_add=True)
    date_updated=models.DateTimeField(verbose_name=("تاريخ التعديل"), auto_now=True)
    
    
    def __str__(self):
        return str(self.patient)


class Rate(models.Model):
    doctor=models.ForeignKey(User ,verbose_name=' اسم الدكتور ', on_delete=models.CASCADE , related_name='doctorRate')
    patient=models.ForeignKey(User ,verbose_name=' اسم المريض ', on_delete=models.CASCADE , related_name='patientRate')
    rate=models.IntegerField(verbose_name=("التقييم"),default=0,validators=[MaxValueValidator(5),MinValueValidator(0)])
    date_created=models.DateTimeField(verbose_name=("تاريخ التعليق"), auto_now_add=True)
    date_updated=models.DateTimeField(verbose_name=("تاريخ التعديل"), auto_now=True)

    def __str__(self):
        return str(self.patient)
    
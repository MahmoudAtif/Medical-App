from django.contrib import admin
from .models import *
from accounts.models import ClinicImages , DoctorServices

# Register your models here.

class ClinicImagesInlines(admin.TabularInline):
    model=ClinicImages

class DoctorServicesInlines(admin.TabularInline):
    model=DoctorServices

class ProfileAdmin(admin.ModelAdmin):
    inlines=[ClinicImagesInlines,DoctorServicesInlines]

admin.site.register(Doctor)
admin.site.register(Specialties)
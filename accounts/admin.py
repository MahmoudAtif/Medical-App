from django.contrib import admin 
from .models import *
# Register your models here.

admin.site.register(Appointment)
admin.site.register(ClinicImages)
admin.site.register(DoctorServices)
admin.site.register(Comment)
admin.site.register(Rate)
from django.shortcuts import render , redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import *
from user.forms import *
from user.models import *
from .models import *
from .filters import FilterForm

# Create your views here.



# @login_required(login_url='login_page')
def index(request):
    doctors=Doctor.objects.all()
    filterForm= FilterForm()
    if request.method=='GET':
        filterForm= FilterForm(request.GET,queryset=doctors)
        doctors=filterForm.qs
    
    context={
        'doctors':doctors,
        'filterForm':filterForm,
    }
    return render(request ,'user/index.html',context)

@login_required(login_url='login_page')
def doctor_list(request):
    return render(request ,'user/doctor_list.html')



@login_required(login_url='login_page')
def appointment(request,slug):
    doctor=Doctor.objects.get(slug=slug)  
    if request.method=='POST':
        form=AppointmentForm(request.POST)
        if form.is_valid():
            Appointment.objects.create(
                doctor=doctor.user,
                patient=request.user,
                details=form.cleaned_data['details'],
                time=form.cleaned_data['time'],
            )
        else:
            messages.warning(request,'Invalid Data')
    else:
        form=AppointmentForm()
    
    context={
        'form':form
    }
    return render(request, 'user/appointment.html',context)




def doctor_detail(request, slug):
    doctor= Doctor.objects.get(slug=slug)
    comments=Comment.objects.filter(doctor=doctor.user)
    if request.user.is_authenticated:
        if request.method =='POST':
            comment_form=CommnetForm(request.POST)
            comment=request.POST.get('comment')

            rate_form=RateForm(request.POST)
            rate=request.POST.get('rate')

            if comment_form.is_valid():
                Comment.objects.create(
                    doctor=doctor.user,
                    patient=request.user,
                    comment=comment,
                    
                )

            if rate_form.is_valid():
                patient_rate=Rate.objects.filter(doctor=doctor.user,patient=request.user)
                if not patient_rate:
                    Rate.objects.create(
                        doctor=doctor.user,
                        patient=request.user,
                        rate=rate,
                    )
                else:
                    patient_rate=Rate.objects.get(doctor=doctor.user,patient=request.user)
                    patient_rate.rate=rate
                    patient_rate.save()     
        else:
            comment_form=CommnetForm()
    else:
        print('login required')
    
    context={
        'doctor':doctor,
        'comments':comments,
    }
    return render(request , 'user/doctors_detail.html',context)



def favourite(request):
    favourites=Doctor.objects.filter(favourite=request.user)
    context={
       'favourites':favourites 
    }
    return render(request , 'user/favourite.html',context)


def add_to_favourite(request,slug):
    doctor=Doctor.objects.get(slug=slug)
    
    if not request.user in doctor.favourite.all():
        doctor.favourite.add(request.user)
    else:
        doctor.favourite.remove(request.user)

    return redirect(request.META['HTTP_REFERER'])
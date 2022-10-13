from email.mime import image
from multiprocessing import context
from django.shortcuts import render , redirect
from django.contrib.auth import authenticate ,login , logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from accounts.decorators import unauthenticated_user
from .forms import *
from .models import Doctor
from accounts.models import *
from django.forms import inlineformset_factory,modelformset_factory

# Create your views here.


@unauthenticated_user
def login_page(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request , username=username , password=password)

        if user is not None:
            login(request , user)
            return redirect('index')
        else:
            messages.info(request, 'Username or password is incorrect')
    
    return render(request , 'user/login.html')


@unauthenticated_user
def signup(request):
    form=UserForm()
    if request.method=='POST':
         form=UserForm(request.POST)
         if form.is_valid():
            form.save()
            messages.success(request , 'Account created Successfully')

    context={
        'form':form,
    }
    return render(request , 'user/signup.html',context)



def logout_page(request):
    logout(request)
    return redirect('login_page')

@login_required(login_url='login_page')
def profile_page(request,slug):
    doctor=Doctor.objects.get(slug=slug)
    context={
       'doctor':doctor
    }
    return render(request , 'user/profile.html',context)

@login_required(login_url='login_page')
def update_profile(request,slug):
    doctor=Doctor.objects.get(slug=slug)
    if request.method=='POST':
        form=ProfileForm(request.POST, request.FILES, instance=doctor)
        if form.is_valid:
            form.save()
        return redirect('profile', slug=doctor.slug)
    else:
        form=ProfileForm(instance=doctor)
    context={
        'form':form,
    }
    return render(request , 'user/update_profile.html',context)



def add_service(request,slug):
    doctor=Doctor.objects.get(slug=slug)
    if request.method=='POST':
        form=ServiceForm(request.POST)
        if form.is_valid():
            DoctorServices.objects.create(
                clinic=doctor,
                service=form.cleaned_data['service'],
            )
            return redirect('profile',slug=doctor.slug)
    else:
        form=ServiceForm()

    context={
        'form':form
    }
    return render(request , 'add_service.html',context=context)


def delete_service(request,id):
    service=DoctorServices.objects.get(id=id)
    service.delete()
    return redirect(request.META['HTTP_REFERER'])



def add_image(request,slug):
    doctor=Doctor.objects.get(slug=slug)
    if request.method=='POST':
        form=ImageForm(request.POST,request.FILES)
        if form.is_valid():
            ClinicImages.objects.create(
                clinic=doctor,
                image=form.cleaned_data['image']
            )
            return redirect('profile',slug=doctor.slug)
    else:
        form=ImageForm()


    context={
        'form':form
    }
    return render(request , 'add_image.html',context=context)



def delete_image(request,id):
    image=ClinicImages.objects.get(id=id)
    image.delete()
    return redirect(request.META['HTTP_REFERER'])


def delete_comment(request , id):
    comment=Comment.objects.get(id=id)
    comment.delete()
    return redirect(request.META['HTTP_REFERER'])

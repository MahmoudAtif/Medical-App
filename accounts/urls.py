from django.urls import path
from . import views
from django.contrib.auth import views as auth_Views
urlpatterns=[
    path('',views.index,name='index'),
    path('doctor_list',views.doctor_list,name='doctor_list'),
   
    path('appointment/<slug:slug>/',views.appointment , name='appointment'),

    path('doctor_detail/<slug:slug>/' , views.doctor_detail , name='doctor_detail'),

    path('add_to_favourite/<slug:slug>' , views.add_to_favourite , name='add_to_favourite'),
    path('favourite' , views.favourite , name='favourite'),


]
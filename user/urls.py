from django.urls import path
from . import views

urlpatterns = [
   
    path('login_page',views.login_page,name='login_page'),
    path('signup',views.signup,name='signup'),
    path('logout_page',views.logout_page,name='logout_page'),

    path('profile_page/<slug:slug>/',views.profile_page,name='profile'),
    path('update_profile/<slug:slug>/',views.update_profile,name='update_profile'),
   
    path('add_service/<slug:slug>/',views.add_service,name='add_service'),
    path('delete_service/<int:id>/',views.delete_service,name='delete_service'),
   
    path('add_image/<slug:slug>/',views.add_image,name='add_image'),
    path('delete_image/<int:id>/',views.delete_image,name='delete_image'),
    path('delete_comment/<int:id>/',views.delete_comment,name='delete_comment'),
]


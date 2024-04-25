from django.urls import path
from .import views


urlpatterns = [
    path('',views.index,name='index'),
     path('index2.html',views.index2,name='index2'),
    path('register.html',views.register,name='register'),
    path('about.html',views.about,name='about'),
    path('vrindavan.html',views.vrindavan,name='vrindavan'),
    path('mathura.html',views.mathura,name='mathura'),
    path('Ayodhya.html',views.ayodhya,name='ayodhya'),
    path('rajasthan.html',views.rajasthan,name='rajasthan'), 
]

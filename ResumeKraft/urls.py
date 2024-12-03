from django.contrib import admin
from django.urls import path

from ResumeKraft import views 
from pdfgeneration import views as v


urlpatterns = [
    path('', views.index,name='index'),
    path('home', views.loginuser,name='login'),
    path('register', views.register,name='register'),
    path('logout', views.logoutuser,name=''),
    path('resume', v.chooseTemplate,name=''),
    path('create', v.createResume,name=''),
    path('faq', views.faq,name=''),
    path('about', views.about,name=''),
    path('contact', views.contact,name=''),
    path('feedback', views.feedback,name=''),

]

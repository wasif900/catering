"""eCatering URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
  
    path('', views.loginPage ,name = 'loginPage'),
    path('register2',views.register2, name="register2"),
    path('register3',views.register3, name="register3"),
    path('register',views.index, name="register1"),
    path('home',views.home , name ='home'),
    path('logout', views.logoutuser , name='logout'),
    path('sellergig', views.sellergig , name='sellergig'),
    path('CreateNewGig', views.createNewGig , name='CreateNewGig'),
    path("gigPricing", views.gigPricing , name="gigPricing"),
    path("gigDescription", views.gigDescription , name="gigDescription"),
    path("gigGallery", views.gigGallery , name="gigGallery"),
    path('search',views.search , name='search'),
    path('searchPage',views.searchPage, name='searchPage')
] 

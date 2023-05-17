from django.shortcuts import render
from django.http import HttpResponse  #new

def index(request): #new
   print("hello")
   return render(request, 'resgister.html')
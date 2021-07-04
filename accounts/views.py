from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.
def home(request):
    context={
        'classes':Grade.objects.all()
    }
    return render(request,'accounts/dashboard.html',context)

def students(request,id):
    context={
        'students':Student.objects.filter(grade=id)
    }
    return render(request,'accounts/students.html',context)
    
def subject(request,id):
    context={
        'subjects':Subject.objects.all(),
        'students':Student.objects.filter(grade=id)

    }
    return render(request,'accounts/subject.html',context)
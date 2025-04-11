from django.shortcuts import render
from django.http import HttpResponse
from .models import Student


def message(request):
    return HttpResponse("Hello, world. You're at the message page.")

def home(request):
    students = Student.objects.all()
    return render(request,'home.html',{'students':students})
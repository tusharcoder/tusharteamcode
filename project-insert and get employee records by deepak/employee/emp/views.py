from django.http import HttpResponse
from django.shortcuts import render, redirect

from .models import employee


def home(request):
    employee_list = employee.objects.all()
    return render(request, 'emp/employeeList.html', context={"employee_list":employee_list})


def insert(request):
    return render(request, 'emp/insert.html')

def doinsert(request):
    employee(fname=request.POST['fname'],lname=request.POST['lname'],sal=request.POST['salary']).save()
    return redirect('/emp/home/')
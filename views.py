from django.shortcuts import render
from django.http import HttpResponse

def content(request):
    return render(request,'site.html')

def one(request):
    return render(request,'01.html')

def two(request):
    return render(request,'02.html')

def three(request):
    return render(request,'03.html')

def four(request):
    return render(request,'04.html')

def five(request):
    return render(request,'05.html')

def six(request):
    return render(request,'06.html')

def seven(request):
    return render(request,'07.html')

def eight(request):
    return render(request,'08.html')

def nine(request):
    return render(request,'09.html')

def ten(request):
    return render(request,'10.html')
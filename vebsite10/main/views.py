from django.shortcuts import render
from django.http import HttpResponse
from .models import Task

def index(request):
    tasks = Task.objects.all()
    return render(request, 'main.html', {'title':'Главная страница'}, {'tasks':tasks})

def Hello(request):
    return HttpResponse("<h3>Приветик :)</h3>")

def about(request):
    return render(request, 'about.html')
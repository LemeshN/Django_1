from django.shortcuts import render
from django.http import HttpResponse
from .models import Task

def main(request):
    tasks = Task.objects.order_by('id')
    return render(request, 'main.html', {'title':'Главная страница', 'tasks':'title'})

def Hello(request):
    return HttpResponse("<h3>Приветик :)</h3>")

def about(request):
    return render(request, 'about.html')

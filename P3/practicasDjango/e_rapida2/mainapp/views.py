from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'mainapp/index.html', {
        'title':'Inicio',
        'content':'Soy Inicio'
    })

def about(request):
    return render(request, 'mainapp/about.html', {
        'title':'Inicio',
        'content':'Soy Acerca De'
    })

def mission(request):
    return render(request, 'mainapp/mission.html', {
        'title':'Inicio',
        'content':'Soy Misión'
    })

def vision(request):
    return render(request, 'mainapp/vision.html', {
        'title':'Inicio',
        'content':'Soy Visión'
    })
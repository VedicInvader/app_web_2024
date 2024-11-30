from django.shortcuts import render, redirect
from mainapp.forms import RegisterForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(requests):
    return render(requests, 'mainapp/index.html',{
        'title':'Inicio',
        'content': 'Soy inicio'
    })

@login_required(login_url='inicio')

def about(requests):
    mensaje='Bienvenido Mi Nombre es Marco Antonio González Espino'
    return render(requests, 'mainapp/about.html', {
        'title': 'Acerca de Nosotros',
        'content':'Somos un grupo de programadores que sabemos lo que hacemos',
        'mensaje': mensaje
    })

@login_required(login_url='inicio')
def mision(requests):
    return render(requests, 'mainapp/mision.html', {
        'title': 'Misión de la Empresa',
        'content':'Nos comprometemos a ser una empresa de calidad y buen servicio',
        
    })

@login_required(login_url='inicio')
def vision(requests):
    return render(requests, 'mainapp/vision.html', {
        'title': 'Nuestra Vision',
        'content':'Nuestra visión es que el cliente se sienta bien',
        
    })

def redir_index (request, exception=None):
    return redirect('index')

def login_user(request):
    if request.user.is_authenticated:
        return redirect('inicio')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')


            user = authenticate(request, username = username, password = password)

            if user is not None:
                login(request, user)
                messages.success(request, "Bienvenido al inicio de sesión")
                return redirect('inicio')
            else:
                messages.warning(request, "No es posible iniciar sesión, por favor ingrese sus credenciales de acceso")
        
    return render(request, 'users/login.html',{
        'title':'Inicio de sesión',
    })

def register_user(request):
    if request.user.is_authenticated:
        return redirect('inicio')
    else:
        register_form=RegisterForm()

        if request.method == "POST":
            register_form=RegisterForm(request.POST)

            if register_form.is_valid():
                register_form.save()
                messages.success(request, "¡Registro exitoso!")
                return redirect('inicio')


        return render(request, 'users/register.html', {
            'title':'Registro de usuario',
            'register_form':register_form
        })

def logout_user(request):
    logout(request)
    return redirect('inicio')
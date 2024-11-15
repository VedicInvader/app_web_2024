from django.shortcuts import render, redirect

# Create your views here.

def index(requests):
    return render(requests, 'mainapp/index.html',{
        'title':'Inicio | Página Principal',
        'content': 'Bienvenidos a la Pagina Principal'
    })

def about(requests):
    mensaje='Bienvenido Mi Nombre es Marco Antonio González Espino'
    return render(requests, 'mainapp/about.html', {
        'title': 'Acerca de Nosotros',
        'content':'Somos un grupo de Programadores que sabemos lo que hacemos',
        'mensaje': mensaje
    })


def mision(requests):
    return render(requests, 'mainapp/mision.html', {
        'title': 'Mision de la Empresa',
        'content':'Nos comprometemos a ser una empresa de calidad y buen servicio',
        
    })


def vision(requests):
    return render(requests, 'mainapp/vision.html', {
        'title': 'Nuestra Vision',
        'content':'Nuestra Vision es que el cliente se sienta bien',
        
    })

def redir_index (request, exception=None):
    return redirect('index')
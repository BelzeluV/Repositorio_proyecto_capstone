from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth import authenticate,login
from Store.models import *
from Store.forms import UserForm


# Create your views here.
def synchronization(request):
    return redirect(to = "inicioBackoffice")

def registroUsuario(request):
    formulario = UserForm
    data = {"form" : formulario}

    if request.method == 'POST':
            formulario = UserForm(data=request.POST, files=request.FILES)
            print("el formulario esta bien?: ", formulario.is_valid())
            if formulario.is_valid():
                formulario.save()
                user = authenticate(username=formulario.cleaned_data["username"],password=formulario.cleaned_data["password1"])
                login(request,user)
                messages.success(request,"Iniciaste sesión correctamente")
                return redirect(to="inicio")
            else:
                print(formulario.errors)
                data["form"] = formulario
                print("hay un error dentro del formulario, por favor corrigalo")

    return render(request, "registration/registro.html", data)

def ValidarUsuario(request):
    if request.user.is_authenticated:
        if request.user.is_superuser :
            return redirect(to = "inicioback")
        if request.user.is_staff:
            return redirect(to = "inicioback")
        else:
            return redirect(to = "inicio")
    return redirect('login')

#pagina del backoffice

def inicioBackoffice(request):
    return render(request, "backoffice/Inicio/InicioBackoffice.html")

def menuCategorias(request):
    categorias = Categoria.objects.all()
    tipo = TipoProducto.objects.all()
    data = {"tipo": tipo, "categorias": categorias}
    return render(request,"backoffice/CRUD_categorias/menu.html", data)

def menuTipoProducto(request):
    return render(request,"backoffice/CRUD_tipoproducto/menu.html")

def menuSubcategorias(request):
    return render(request,"backoffice/CRUD_subcategorias/menu.html")

from django.shortcuts import render,HttpResponse,redirect
from .models import Equipo
from .forms import equipoForm, CustomUserForm
from django.contrib.auth import login,authenticate


# Create your views here.

def login_usuario(request):
    return render(request,"registration/login.html")

#def base(request):
#    return render(request,"core/base.html")|
def autentificar(request):
    try:
        from django.contrib.auth import authenticate
        login=request.POST.get('login')
        password=request.POST.get('password')
        print("login "+login)
        print("password "+password)
        user = authenticate(username=login, password=password)
        print(user)
        if user ==None:
            raise Exception("Usuario y Contrasenia no son validos")
        return home(request)
    except Exception as ex:
        return render(request,"core/login.html",context={"error":ex}) 


def loginNuevo(request):
    data ={
        'form':CustomUserForm()
    }

    if request.method == 'POST':
        formulario = CustomUserForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            username= formulario.cleaned_data['username']
            password = formulario.cleaned_data['password1']
            user= authenticate(username=username, password=password)
            login(request,user)
            return redirect(to='login')
   
    return render(request,"registration/login-nuevo.html",data)

def home(request):
    return render(request,"core/home.html")

def equipos(request):
    data ={
        'equipos':Equipo.objects.all()
    }
    return render(request,"core/equipos.html",data)

def calendario(request):
    return render(request,"core/calendario.html")
    
def nosotros(request):
    return render(request,"core/nosotros.html")

def listadoEquipo(request):
    equipos = Equipo.objects.all()
    data={
        'equipos':equipos
    }

    return render(request,"core/listado_equipos.html",data)



def nuevoEquipo(request):
    data = {
        'form':equipoForm()
    }

    if request.method == 'POST':
        formulario = equipoForm(request.POST,files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = "Guardado correctamente"

    return render(request,"core/nuevo_equipo.html",data)

def modificar_equipo(request,id):
    equipos = Equipo.objects.get(id=id)
    data = {
        'form':equipoForm(instance=equipos)
    }

    if request.method == 'POST':
        formulario = equipoForm(data=request.POST,instance=equipos,files=request.FILES)

        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = "Modificado correctamente"
            data['form'] = equipoForm(instance=Equipo.objects.get(id=id))

    
    return render(request,"core/modificar_equipo.html",data)


def eliminar_equipo(request,id):
    equipos = Equipo.objects.get(id=id)
    equipos.delete()

    return redirect(to="listado_equipos")
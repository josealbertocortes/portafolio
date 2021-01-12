from django.shortcuts import render

# Create your views here.
def perfil(request):

    return render(request,'perfil/index.html')

def trabajos(request):

    return render(request,'perfil/trabajos.html')

def estudios(request):

    return render(request,'perfil/estudios.html')
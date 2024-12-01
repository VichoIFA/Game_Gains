from django.shortcuts import render, redirect
from . import models

def Homepage(request):
    return render(request, 'Homepage.html')

def Login(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')

        if username == 'admin' and password == '1234':
            return redirect('DashboardComprador.html') 
        if username == 'trabajadorCiudad_A' and password == 'ciudadA':
            return redirect('DashboardComprador.html')
        if username == 'trabajadorCiudad_B' and password == 'ciudadB':
            return redirect('DashboardComprador.html')        
        if username == 'trabajadorCiudad_C' and password == 'ciudadC':
            return redirect('DashboardComprador.html')
        else:
            return render(request, 'Login.html', {'error': 'Usuario o contraseña incorrectos'})
    return render(request, 'Login.html')

def Comprador(request):
    
    TiposProductos = ["Espadas", "Armaduras", "Pociones", "Arcos", "Escudos", "Anillos", "Amuletos"]

    PrecioPromedio = models.PrecioPromedioPorTipo(5)
    StockTotal = models.StockEnMercadoTotal(5)
    CantidadPorTipo = models.CantidadDisponiblePorTipo(5)
    print(CantidadPorTipo)
    
    context = {
        "PrecioPromedio" : PrecioPromedio,
        "StockTotal" : StockTotal,
        "CantidadPorTipo" : CantidadPorTipo
    }
    return render(request, 'DashboardComprador.html', context)

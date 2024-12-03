from django.shortcuts import render, redirect
from . import models

def Homepage(request):
    return render(request, 'Homepage.html')

def Login(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')

        if username == 'admin' and password == '1234':
            return redirect('DashboardInicial') 
        if username == 'Comprador' and password == '1234':
            return redirect('Comprador')
        if username == 'Vendedor' and password == '1234':
            return redirect('Vendedor')        
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

def DashboardComprador(request, producto,precio):
        
    TiposProductos = ["Espadas", "Armaduras", "Pociones", "Arcos", "Escudos", "Anillos", "Amuletos"]
    posicion = TiposProductos.index(producto)+1
    PrecioPromedio = models.PrecioPromedioPorTipo(posicion)
    StockTotal = models.StockEnMercadoTotal(posicion)
    CantidadPorTipo = models.CantidadDisponiblePorTipo(posicion)
    DatosRareza = models.CantidadPorRareza(posicion)
    DatosMercado = models.CantidadPorMercado(posicion)
    nombreRareza,cantidadRareza,nombreMercado,cantidadMercado = [],[],[],[]
    
    for x in DatosRareza:
        nombreRareza.append(x[0])
        cantidadRareza.append(int(x[1]))
        
    for x in DatosMercado:
        cantidadMercado.append(x[0])
        nombreMercado.append(int(x[1]))
    
    
    context = {
        "PrecioPromedio" : PrecioPromedio,
        "StockTotal" : StockTotal,
        "CantidadPorTipo" : CantidadPorTipo,
        "cantidadRareza" : cantidadRareza,
        "nombreRareza" : nombreRareza,
        "cantidadMercado" : cantidadMercado,
        "nombreMercado" : nombreMercado,
        "producto" : producto
    }
    return render(request, 'DashboardComprador.html', context)



def ProfundizacionMercado(request, producto, mercado):
    colores = ["#0033ff", "#1100ff", "#6f00ff","#b300ff"]
    
    TiposProductos = ["Espadas", "Armaduras", "Pociones", "Arcos", "Escudos", "Anillos", "Amuletos"]
    mercados = ["Mercado Central", "Mercado del Bosque","Mercado del Norte","Mercado del Este","Mercado Oscuro"]
    posicion = TiposProductos.index(producto)+1
    mercadoSeleccionado = mercados[mercado]
    PosicionMercado = mercado+1
    
    
    #cantidadItem = models.CantidadMercadoEspecifico(posicion, PosicionMercado)
    precioPromedio = float(models.PrecioPromedioItemMercado(posicion, PosicionMercado))
    datosRarezas = models.CantidadRarezaPorMercado(posicion,PosicionMercado)
    rarezas, cantidadRarezas = [],[]
    for x in datosRarezas:
        rarezas.append(x[0])
        cantidadRarezas.append(int(x[1]))
        
    context = {
        "PrecioPromedio" : precioPromedio,
        "Mercado" : mercadoSeleccionado,
        "Rarezas" : rarezas,
        "CantidadRarezas" : cantidadRarezas
    }
    return render(request, 'detalleProductoMercadoComprador.html', context)

def ProfundizacionRareza(request, producto, rareza):
    
    colores = ["#0033ff", "#1100ff", "#6f00ff","#b300ff"]
    rarezas = ["comunes","raros","legendarios","míticos"]
    rarezasFiltro = ["Común","Raro","Legendario","Mítico"]
    
    #cantidadItemsDistintos = models.CantidadPorRarezaItemsDistintos(producto)
    
    rarezaSeleccionada = rarezas[rareza]
    color = colores[rareza]
    
    context = {
        "Rareza" : rarezaSeleccionada,
        "color" : color
    }
    return render(request, 'detalleRarezaComprador.html', context)



def Comprador(request):    
    return render(request, 'Comprador.html')

def Vendedor(request):
    return render(request, 'Vendedor.html')


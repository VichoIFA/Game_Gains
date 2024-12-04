from django.shortcuts import render, redirect
from django.templatetags.static import static
from . import models
import random

def Homepage(request):
    return render(request, 'Homepage.html')

def Login(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')

    return render(request, 'Login.html')

def DashboardComprador(request, producto, precio):
        
    TiposProductos = ["Espadas", "Armaduras", "Pociones", "Arcos", "Escudos", "Anillos", "Amuletos"]
    escogerImagen = {
        0: [static('images/espada1.png'), static('images/espada2.png'), static('images/espada3.png')],
        1: [static('images/armadura1.png'), static('images/armadura2.webp'), static('images/armadura3.png')],
        2: [static('images/pocion1.webp'), static('images/pocion2.png'), static('images/pocion3.png')],
        3: [static('images/arco1.png'), static('images/arco2.png'), static('images/arco3.png')],
        4: [static('images/escudo1.png'), static('images/escudo2.png'), static('images/escudo3.png')],
        5: [static('images/anillo1.png'), static('images/anillo2.png'), static('images/anillo3.png')],
        6: [static('images/amuleto1.png'), static('images/amuleto2.png'), static('images/amuleto3.png')],
    }

    
    rangoPrecio = precio.split('-')
    rangoPrecio = [int(x) for x in rangoPrecio]
    

    
    precioPromedio = sum(rangoPrecio)/len(rangoPrecio)
    print(precioPromedio)
    
    posicion = TiposProductos.index(producto)
    imagen = random.choice(escogerImagen[posicion])
    
    posicion += 1
    PrecioPromedio = models.PrecioPromedioPorTipo(posicion)
    
    CotaSup = precioPromedio + precioPromedio*0.3
    CotaInf = precioPromedio - precioPromedio*0.3
    
    if CotaInf <= PrecioPromedio <= CotaSup:
        
        color = '#024f01'
    else:
        color = '#a10202'
        
        
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
        "producto" : producto,
        "rutaImagen" : imagen,
        "color" : color
    }
    return render(request, 'DashboardComprador.html', context)

def ProfundizacionMercado(request, producto, mercado):
    
    colores = ["#0033ff", "#1100ff", "#6f00ff","#b300ff"]
    
    TiposProductos = ["Espadas", "Armaduras", "Pociones", "Arcos", "Escudos", "Anillos", "Amuletos"]
    mercados = ["Mercado Central", "Mercado del Bosque","Mercado del Norte","Mercado del Este","Mercado Oscuro"]
    posicion = TiposProductos.index(producto)+1
    mercadoSeleccionado = mercados[mercado]
    PosicionMercado = mercado+1
    
    
    ubicacion = models.UbicacionMercado(posicion, PosicionMercado)
    precioPromedio = float(models.PrecioPromedioItemMercado(posicion, PosicionMercado))
    datosRarezas = models.CantidadRarezaPorMercado(posicion,PosicionMercado)
    rarezas, cantidadRarezas = [],[]
    for x in datosRarezas:
        rarezas.append(x[0])
        cantidadRarezas.append(int(x[1]))
        
    context = {
        "ubicacionMercado" : ubicacion,
        "PrecioPromedio" : precioPromedio,
        "Mercado" : mercadoSeleccionado,
        "Rarezas" : rarezas,
        "CantidadRarezas" : cantidadRarezas
    }
    return render(request, 'detalleProductoMercadoComprador.html', context)

def ProfundizacionRareza(request, producto, rareza):
    
    colores = ["#0033ff", "#1100ff", "#6f00ff","#b300ff"]
    rarezas = ["comunes","raros","legendarios","míticos"]
    items = ["Espadas", "Armaduras", "Pociones", "Arcos", "Escudos", "Anillos", "Amuletos"]
    rarezasFiltro = ["Común","Raro","Legendario","Mítico"]
    
    #cantidadItemsDistintos = models.CantidadPorRarezaItemsDistintos(producto)
    posicion = items.index(producto)+1
    
    rarezaSeleccionada = rarezas[rareza]
    rarezaSeleccionadaProdecure = rarezasFiltro[rareza]
    
    print(posicion)
    print(rarezaSeleccionada)
    cantidadItemsDistintos = models.CantidadPorRarezaItemsDistintos(posicion,rarezaSeleccionadaProdecure)
    precioPromedioRareza = models.PrecioPromedioPorRareza(posicion,rarezaSeleccionadaProdecure)
    DatosTiempo = models.CantidadRarezaPorTiempo(posicion, rarezaSeleccionadaProdecure)
    
    precioPromedio = precioPromedioRareza[2]
    variedadItems = cantidadItemsDistintos[2]
    tiempo, cantidad = [],[]
    
    for x in DatosTiempo:
        tiempo.append(x[0])
        cantidad.append(x[1])
    
    color = colores[rareza]
    
    context = {
        "Rareza" : rarezaSeleccionada,
        "color" : color,
        "variedadItems" : variedadItems,
        "precioPromedio" : precioPromedio,
        "tiempoObtencion" : tiempo,
        "cantidad" : cantidad
    }
    return render(request, 'detalleRarezaComprador.html', context)

def DashboardVendedor(request, producto, precio, cantidad, rareza):
    TiposProductos = ["Espadas", "Armaduras", "Pociones", "Arcos", "Escudos", "Anillos", "Amuletos"]
    escogerImagen = {
        0: [static('images/espada1.png'), static('images/espada2.png'), static('images/espada3.png')],
        1: [static('images/armadura1.png'), static('images/armadura2.webp'), static('images/armadura3.png')],
        2: [static('images/pocion1.webp'), static('images/pocion2.png'), static('images/pocion3.png')],
        3: [static('images/arco1.png'), static('images/arco2.png'), static('images/arco3.png')],
        4: [static('images/escudo1.png'), static('images/escudo2.png'), static('images/escudo3.png')],
        5: [static('images/anillo1.png'), static('images/anillo2.png'), static('images/anillo3.png')],
        6: [static('images/amuleto1.png'), static('images/amuleto2.png'), static('images/amuleto3.png')],
    }
    
    posicion = TiposProductos.index(producto)
    imagen = random.choice(escogerImagen[posicion])
    posicion += 1
    DemandaTotal = models.DemandaTotal(posicion)    
    demanda = DemandaTotal[1]
    PrecioPromedio = models.PrecioPromedioPorTipo(posicion)
    CotaSup = precio + precio*0.2
    CotaInf = precio - precio*0.2
    
    if CotaInf <= PrecioPromedio <= CotaSup:
        color = '#024f01'
    else:
        color = '#a10202'
    StockTotal = models.StockEnMercadoTotal(posicion)
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
        "demanda" : demanda,
        "cantidadRareza" : cantidadRareza,
        "nombreRareza" : nombreRareza,
        "cantidadMercado" : cantidadMercado,
        "nombreMercado" : nombreMercado,
        "producto" : producto,
        "rutaImagen" : imagen,
        "color" : color
    }
    return render(request, 'DashboardVendedor.html', context)

def ProfundizacionRarezaVededor(request, producto, rareza):
    
    colores = ["#0033ff", "#1100ff", "#6f00ff","#b300ff"]
    rarezas = ["comunes","raros","legendarios","míticos"]
    items = ["Espadas", "Armaduras", "Pociones", "Arcos", "Escudos", "Anillos", "Amuletos"]
    rarezasFiltro = ["Común","Raro","Legendario","Mítico"]
    
    #cantidadItemsDistintos = models.CantidadPorRarezaItemsDistintos(producto)
    posicion = items.index(producto)+1
    
    rarezaSeleccionada = rarezas[rareza]
    rarezaSeleccionadaProdecure = rarezasFiltro[rareza]
    
    print(posicion)
    print(rarezaSeleccionada)
    cantidadItemsDistintos = models.CantidadPorRarezaItemsDistintos(posicion,rarezaSeleccionadaProdecure)
    precioPromedioRareza = models.PrecioPromedioPorRareza(posicion,rarezaSeleccionadaProdecure)
    DatosTiempo = models.CantidadRarezaPorTiempo(posicion, rarezaSeleccionadaProdecure)
    
    precioPromedio = precioPromedioRareza[2]
    variedadItems = cantidadItemsDistintos[2]
    tiempo, cantidad = [],[]
    
    for x in DatosTiempo:
        tiempo.append(x[0])
        cantidad.append(x[1])
    
    color = colores[rareza]
    
    context = {
        "Rareza" : rarezaSeleccionada,
        "color" : color,
        "variedadItems" : variedadItems,
        "precioPromedio" : precioPromedio,
        "tiempoObtencion" : tiempo,
        "cantidad" : cantidad
    }
    return render(request, 'detalleRarezaVendedor.html', context)


def ProfundizacionMercadoVendedor(request, producto, mercado):
    
    colores = ["#0033ff", "#1100ff", "#6f00ff","#b300ff"]
    
    TiposProductos = ["Espadas", "Armaduras", "Pociones", "Arcos", "Escudos", "Anillos", "Amuletos"]
    mercados = ["Mercado Central", "Mercado del Bosque","Mercado del Norte","Mercado del Este","Mercado Oscuro"]
    posicion = TiposProductos.index(producto)+1
    mercadoSeleccionado = mercados[mercado]
    PosicionMercado = mercado+1
    
    DatosDemanda = models.DemandaPorMercado(posicion, PosicionMercado)
    demandaLocal = int(DatosDemanda[2])
    precioPromedio = float(models.PrecioPromedioItemMercado(posicion, PosicionMercado))
    datosRarezas = models.CantidadRarezaPorMercado(posicion,PosicionMercado)
    rarezas, cantidadRarezas = [],[]
    for x in datosRarezas:
        rarezas.append(x[0])
        cantidadRarezas.append(int(x[1]))
        
    context = {
        "demandaLocal" : demandaLocal,
        "PrecioPromedio" : precioPromedio,
        "Mercado" : mercadoSeleccionado,
        "Rarezas" : rarezas,
        "CantidadRarezas" : cantidadRarezas
    }
    return render(request, 'detalleProductoMercadoVendedor.html', context)


def Comprador(request):    
    return render(request, 'Comprador.html')

def Vendedor(request):
    return render(request, 'Vendedor.html')


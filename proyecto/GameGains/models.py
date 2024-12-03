from django.db import models
from django.db import connection


class Jugador(models.Model):
    idpersona = models.AutoField(db_column='idPersona', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'jugador'


class Jugadormercado(models.Model):
    idpersona = models.OneToOneField(Jugador, models.DO_NOTHING, db_column='idPersona', primary_key=True)  # Field name made lowercase. The composite primary key (idPersona, idMercado) found, that is not supported. The first column is selected.
    idmercado = models.ForeignKey('Mercado', models.DO_NOTHING, db_column='idMercado')  # Field name made lowercase.
    compra = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jugadormercado'
        unique_together = (('idpersona', 'idmercado'),)


class Jugadorproducto(models.Model):
    idpersona = models.OneToOneField(Jugador, models.DO_NOTHING, db_column='idPersona', primary_key=True)  # Field name made lowercase. The composite primary key (idPersona, idProducto) found, that is not supported. The first column is selected.
    idproducto = models.ForeignKey('Producto', models.DO_NOTHING, db_column='idProducto')  # Field name made lowercase.
    cantidad = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jugadorproducto'
        unique_together = (('idpersona', 'idproducto'),)


class Mercado(models.Model):
    idmercado = models.AutoField(db_column='idMercado', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(max_length=80)
    ubicacion = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mercado'


class Producto(models.Model):
    idproducto = models.AutoField(db_column='idProducto', primary_key=True)  # Field name made lowercase.
    idtipoproducto = models.ForeignKey('Tipoproducto', models.DO_NOTHING, db_column='idTipoProducto')  # Field name made lowercase.
    tiempoobtencion = models.IntegerField(db_column='tiempoObtencion', blank=True, null=True)  # Field name made lowercase.
    adquisicion = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'producto'


class Productomercado(models.Model):
    idmercado = models.OneToOneField(Mercado, models.DO_NOTHING, db_column='idMercado', primary_key=True)  # Field name made lowercase. The composite primary key (idMercado, idProducto) found, that is not supported. The first column is selected.
    idproducto = models.ForeignKey(Producto, models.DO_NOTHING, db_column='idProducto')  # Field name made lowercase.
    demanda = models.IntegerField(blank=True, null=True)
    competencia = models.IntegerField(blank=True, null=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'productomercado'
        unique_together = (('idmercado', 'idproducto'),)


class Tipoproducto(models.Model):
    idtipoproducto = models.AutoField(db_column='idTipoProducto', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'tipoproducto'

def PrecioPromedioPorTipo(categoria):
    with connection.cursor() as cursor:
        params = [categoria]
        cursor.callproc('obtener_precio_promedio_por_tipo', params)
        result = cursor.fetchall()
        total = result[0][0]
    return total

def StockEnMercadoTotal(categoria):
    with connection.cursor() as cursor:
        params = [categoria]
        cursor.callproc('obtener_stock_total_por_tipo_producto', params)
        result = cursor.fetchall()
        total = result[0][0]
    return total

def CantidadDisponiblePorTipo(categoria):
    with connection.cursor() as cursor:
        params = [categoria]
        cursor.callproc('obtener_cantidad_total_por_tipo_producto', params)
        result = cursor.fetchall()
        total = result[0][0]
    return total

def CantidadPorRareza(categoria):
    with connection.cursor() as cursor:
        params = [categoria]
        cursor.callproc('obtener_cantidad_por_tipo_producto_y_rareza', params)
        result = cursor.fetchall()
        total = [list(row) for row in result]
    return total

def CantidadPorMercado(categoria):
    with connection.cursor() as cursor:
        params = [categoria]
        cursor.callproc('obtener_cantidad_por_tipo_producto_por_mercado', params)
        result = cursor.fetchall()
        total = [list(row) for row in result]
    return total

"""
def CantidadMercadoEspecifico(categoria, mercado):
    with connection.cursor() as cursor:
        params = [categoria, mercado]
        cursor.callproc('obtener_stock_por_tipo_producto_y_mercado', params)
        result = cursor.fetchall()
        total = [list(row) for row in result]
    return total
"""

def PrecioPromedioItemMercado(categoria, mercado):
    with connection.cursor() as cursor:
        params = [categoria, mercado]
        cursor.callproc('obtener_precio_promedio_por_tipo_producto_y_mercado', params)
        result = cursor.fetchall()
        total = result[0][0]
    return total

def CantidadRarezaPorMercado(categoria, mercado):
    with connection.cursor() as cursor:
        params = [categoria, mercado]
        cursor.callproc('obtener_cantidad_por_rareza_y_mercado', params)
        result = cursor.fetchall()
        total = [list(row) for row in result]
    return total

def CantidadPorRarezaItemsDistintos(categoria, mercado):
    with connection.cursor() as cursor:
        params = [categoria, mercado]
        cursor.callproc('obtener_cantidad_por_tipo_y_rareza', params)
        result = cursor.fetchall()
        total = [list(row) for row in result]
    return total

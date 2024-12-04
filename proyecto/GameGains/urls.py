from django.urls import path
from . import views

urlpatterns = [
    path('', views.Homepage, name='Homepage'),
    path('Login', views.Login, name='Login'),
    path('Comprador/', views.Comprador, name='Comprador'),
    path('Vendedor/', views.Vendedor, name='Vendedor'),
    path('DashboardComprador/<str:producto>/<str:precio>', views.DashboardComprador, name='DashboardComprador'),
    path('detalleRarezaComprador/<str:producto>/<int:rareza>', views.ProfundizacionRareza, name="Rareza"),
    path('detalleProductoMercado/<str:producto>/<int:mercado>', views.ProfundizacionMercado, name="Mercado"),
    path('DashboardVendedor/<str:producto>/<int:precio>/<int:cantidad>/<str:rareza>', views.DashboardVendedor, name= "DashboardVendedor"),
    path('detalleRarezaVendedor/<str:producto>/<int:rareza>', views.ProfundizacionRarezaVededor, name="Rareza"),
    path('detalleProductoMercadoVendedor/<str:producto>/<int:mercado>', views.ProfundizacionMercadoVendedor, name="Mercado"),
]

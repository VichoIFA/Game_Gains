from django.shortcuts import render, redirect

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
        else:
            return render(request, 'Login.html', {'error': 'Usuario o contraseña incorrectos'})
    return render(request, 'Login.html')

def Comprador(request):
    return render(request, 'Comprador.html')

def Vendedor(request):
    return render(request, 'Vendedor.html')
from django.shortcuts import render, redirect

def Homepage(request):
    return render(request, 'Homepage.html')

def Login(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')

        if username == 'admin' and password == '1234':
            return redirect('DashboardInicial') 
        if username == 'trabajadorCiudad_A' and password == 'ciudadA':
            return redirect('DashboardUsuarioCiudad/A')
        if username == 'trabajadorCiudad_B' and password == 'ciudadB':
            return redirect('DashboardUsuarioCiudad/B')        
        if username == 'trabajadorCiudad_C' and password == 'ciudadC':
            return redirect('DashboardUsuarioCiudad/B')
        else:
            return render(request, 'Login.html', {'error': 'Usuario o contraseña incorrectos'})
    return render(request, 'Login.html')

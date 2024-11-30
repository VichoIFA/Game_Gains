from django.shortcuts import render, redirect
def Homepage(request):
    return render(request, 'Homepage.html')

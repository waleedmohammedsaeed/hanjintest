from django.shortcuts import render

# Create your views here.

def energy(request):
    return render(request, 'energy.html')

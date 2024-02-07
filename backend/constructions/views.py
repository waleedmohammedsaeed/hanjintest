from django.shortcuts import render

# Create your views here.

def constructions(request):
    return render(request, 'constructions.html')

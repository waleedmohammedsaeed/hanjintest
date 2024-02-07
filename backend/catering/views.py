from django.shortcuts import render
# from .models import 
# from .serializers import BranchSerializer, CategorySerializer
# from rest_framework import generics
from django.http import JsonResponse
from rest_framework.decorators import api_view

# Create your views here.

def catery(request):
    return render(request, 'catering.html')

def cafteria(request):
    return render(request, 'cafeteria.html')

def koreanfood(request):
    return render(request, 'koreanfood.html')

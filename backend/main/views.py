from django.shortcuts import render
from .models import Branch, Category
from .serializers import BranchSerializer, CategorySerializer
# from rest_framework import generics
from django.http import JsonResponse
from rest_framework.decorators import api_view

# Create your views here.

def home(request):
    branches= Branch.objects.all()
    return render(request, 'home.html')
def catering(request):
    branches= Branch.objects.all()
    return render(request, 'catering.html')
def constructions(request):
    branches= Branch.objects.all()
    return render(request, 'constructions.html')
def energy(request):
    branches= Branch.objects.all()
    return render(request, 'energy.html')
def entertainment(request):
    branches= Branch.objects.all()
    return render(request, 'entertainment.html')
def marketing(request):
    branches= Branch.objects.all()
    return render(request, 'marketing.html')

    return render(request, 'home.html',{'branches': branches})
    # ser = BranchSerializer(branches, many=True)
    # return JsonResponse({'data': ser.data})

# @api_view(['POST', 'GET'])
# def category(request):
#     if request.method == 'GET':
#         cat = Category.objects.all()
#         ser = CategorySerializer(cat, many=True)
#         return JsonResponse({'data': ser.data})
#     elif request.method == 'POST':
#         serializer = CategorySerializer(data=request.data)
#         data = {}
#         if serializer.is_valid():
#             serializer.save()
#         return JsonResponse(data)

        
# @api_view(['GET','PUT', 'DELETE'])
# def delete_category(request, id):
#     if request.method == 'PUT':
#         cat = Category.objects.get(id=id)
#         serial = CategorySerializer(cat = request.data)
#         if serial.is_valid():
#             serial.save()
#             return  JsonResponse(serial.data)
#         else:
#             return  JsonResponse(serial.errors)
#     elif request.method == 'DELETE':
#         obj = Category.objects.get(id=id)
#         obj.delete()
#         return JsonResponse("delete category")


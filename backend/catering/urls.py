from django.urls import path
from . import views 

urlpatterns = [
    path('', views.catery, name='catery'),
    path('cafteria/', views.cafteria, name='cafteria'),
    path('koreanfood/', views.koreanfood, name='koreanfood'),

]